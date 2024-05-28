from django.contrib import admin

from articles.forms import ArticleForm
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm


admin.site.register(Article, ArticleAdmin)
