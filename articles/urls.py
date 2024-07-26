from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleDownloadView

app_name = 'articles'
urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/download', ArticleDownloadView.as_view(), name='download'),
]
