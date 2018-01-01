from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Article, Reporter

class ArticleDetail(admin.ModelAdmin):
    list_display = ('id', 'heading', 'created', 'reporter')
    search_fields = ('heading', 'created')

admin.site.register(Article, ArticleDetail)

class ReporterDetail(admin.ModelAdmin):
    list_display = ('id', 'name', 'n_articles')
    search_fields = ('name',)

admin.site.register(Reporter, ReporterDetail)
