import datetime
from django.utils import timezone
from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    slug = models.SlugField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class Author(models.Model):
    author_name = models.CharField(max_length=40)
    author_back = models.TextField()
    
    def __unicode__(self):
        return self.author_name


    
class Site(models.Model):
    LOW = 0
    MED = 1
    HIGH = 2
    TOP = 3
    STATUS_CHOICES = (
                      (LOW, 'low'),
                      (MED, 'medium'),
                      (HIGH, 'high'),
                      (TOP, 'top'),
                      )
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=30)
    url = models.URLField()
    weekly_rating = models.IntegerField(choices=STATUS_CHOICES, default=LOW)
    site_description = models.TextField()
    review_img = models.ImageField(upload_to="img/")
    
    def __unicode__(self):
        return self.name
    
    
class SiteFeatures(models.Model):
    site = models.ForeignKey(Site)
    feature = models.CharField(max_length=200)
    has_feature = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.feature
    

class Banner(models.Model):
    LOW = 0
    MED = 1
    HIGH = 2
    SLIDE = 3
    STATUS_CHOICES = (
                      (LOW, 'low'),
                      (MED, 'medium'),
                      (HIGH, 'high'),
                      (SLIDE, 'slide'),
                      )
    
    site = models.ForeignKey(Site)
    banner_size = models.IntegerField(choices=STATUS_CHOICES, default=LOW)
    banner_image = models.ImageField(upload_to="img/")
    short_text = models.CharField(max_length=500)
    
    
    def __unicode__(self):
        return self.site.name
    

class Article(models.Model):
    author = models.ForeignKey(Author)
    article_headline = models.CharField(max_length=255)
    article_text = models.TextField()
    article_image = models.ImageField(upload_to="img/")
    date_published = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.article_headline
    
    def is_new(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=7)
    
    

    
    
    
    
    
    
    
