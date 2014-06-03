# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'affinal_site_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'affinal_site', ['Category'])

        # Adding model 'Author'
        db.create_table(u'affinal_site_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('author_back', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'affinal_site', ['Author'])

        # Adding model 'Article'
        db.create_table(u'affinal_site_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['affinal_site.Category'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['affinal_site.Author'])),
            ('article_title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('article_headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('article_text', self.gf('django.db.models.fields.TextField')()),
            ('article_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'affinal_site', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'affinal_site_category')

        # Deleting model 'Author'
        db.delete_table(u'affinal_site_author')

        # Deleting model 'Article'
        db.delete_table(u'affinal_site_article')


    models = {
        u'affinal_site.article': {
            'Meta': {'object_name': 'Article'},
            'article_headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'article_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'article_text': ('django.db.models.fields.TextField', [], {}),
            'article_title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['affinal_site.Author']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['affinal_site.Category']"}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'affinal_site.author': {
            'Meta': {'object_name': 'Author'},
            'author_back': ('django.db.models.fields.TextField', [], {}),
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'affinal_site.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['affinal_site']