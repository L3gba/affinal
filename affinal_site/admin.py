from django.contrib import admin
from affinal_site.models import MainCategory, Category, Article, Author, Banner, Site, SiteFeatures

class MainCategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'description']
    

class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_name', 'author_back']

    
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Article Meta', {'fields': ['author', 'article_headline', 'article_text', 'article_image', 'date_published']}),
                 ]
    
class BannerAdmin(admin.ModelAdmin):
    fields = ['site', 'banner_image', 'banner_size', 'short_text']
    

class SiteFeaturesInline(admin.StackedInline):
    model = SiteFeatures
    extra = 4
    
    
class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['category', 'name', 'url', 'weekly_rating',]}),
                 ('Description', {'fields': ['site_description', 'review_img']})
                 ]
    inlines = [SiteFeaturesInline]
    
    

admin.site.register(MainCategory, MainCategoryAdmin)    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Site, SiteAdmin)
