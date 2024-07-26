from django.contrib import admin

from articles.forms import ArticleForm
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'author',)
    list_filter = ('created_at', 'updated_at', 'author',)
    search_fields = ('title', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(Article, ArticleAdmin)
