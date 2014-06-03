from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       # ex: /articles/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # ex: /articles/betting 101/
                       url(r'^betting-101/$', views.ArticlesView.as_view(), name='articles'),
                       # ex: /articles/5/
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='single'),
                       url(r'^sportsbook/$', views.ReviewView.as_view(), name='cat'),
                       url(r'^sportsbook/(?P<pk>\d+)/$', views.ReviewView.as_view(), name='site_review'),
                       url(r'^(?P<slug>[-\w]+)/', views.ReviewView.as_view(), name='online_banking'),
                       url(r'^online-banking/(?P<pk>\d+)/$', views.ReviewView.as_view(), name='whatnot'),
                       )
                       
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))                       