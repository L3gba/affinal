from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.detail import SingleObjectMixin

from models import Article, Site, Banner, Category, SiteFeatures

class IndexView(generic.ListView):
    template_name = 'articles/index3.html'
    context_object_name = 'latest_article_list'
    
    def get_queryset(self):
        """Return the last 5 published articles."""
        return Article.objects.order_by('-date_published')[:5]
    
    def get_context_data(self):
        topsites = Site.objects.filter(weekly_rating__gte=2)
        top3 = Site.objects.filter(weekly_rating=3)
        context = super(IndexView, self).get_context_data()
        context['small_banner_list'] = Banner.objects.filter(site__in=topsites, banner_size=1)
        context['top3_banner_list'] = Banner.objects.filter(site__in=top3, banner_size=0)[:3]
        context['slides_list'] = Banner.objects.filter(banner_size=3)
        context['categories'] = Category.objects.all
        
        return context
        

class ArticlesView(generic.ListView):
    template_name = 'articles/articles.html'
    context_object_name = 'latest_articles'
    
    def get_queryset(self):
        """Return the last published articles"""
        return Article.objects.order_by('-date_published')[:5]
    
    def get_context_data(self):
        topsites = Site.objects.filter(weekly_rating__gte=2)
        context = super(ArticlesView, self).get_context_data()
        context['categories'] = Category.objects.all
        context['small_banner_list'] = Banner.objects.filter(site__in=topsites, banner_size=1)
        
        return context
        

    
class DetailView(generic.DetailView):
    model = Article
    template_name = 'articles/single.html'
    context_object_name = 'single_article'
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data()
        context['categories'] = Category.objects.all
        
        return context
    
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get("pk")
        queryset = queryset.filter(pk=pk)
        obj = queryset.get()
        
        return obj
    
class SportsbookView(generic.ListView):
    model = Site
    template_name = 'articles/site_list.html'
    context_object_name = 'sportsbook_list'
    
    def get_queryset(self):
        return Site.objects.filter(category=1)
    
    def get_context_data(self, **kwargs):
        context = super(SportsbookView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all
        context['features'] = SiteFeatures.objects.filter(site_id=self.kwargs.get("pk"))
        
        return context
    
    
class ReviewView(generic.DetailView):
    model = Site
    template_name = 'articles/review.html'
    context_object_name = 'site_review'
    
    def get_queryset(self):
        return Site.objects.all()
    
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get("pk")
        slug = self.kwargs.get("slug")
        if pk is None and slug is None:
            queryset = queryset.filter(pk=1)
        elif pk is None and slug is not None:
            queryset = queryset.filter(pk=4)
        else:
            queryset = queryset.filter(pk=pk)
            
        obj = queryset.get()
        
        return obj
    
    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        
        if self.kwargs.get("slug") != "online-banking":
            context['site_list'] = Site.objects.filter(category=1)
        else:
            context['site_list'] = Site.objects.filter(category=2)
        
        if self.kwargs.get("pk") is None and self.kwargs.get("slug") is None:
            context['features'] = SiteFeatures.objects.filter(site_id=1)
        elif self.kwargs.get("slug") == "online-banking":
            context['features'] = SiteFeatures.objects.filter(site_id=4)
        else:
            context['features'] = SiteFeatures.objects.filter(site_id=self.kwargs.get("pk"))
            
        context['categories'] = Category.objects.all
        
        return context
        
        
    