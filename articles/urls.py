from django.urls import path

from .views import HomePageView, ArticleListView

app_name = 'articles'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='articles'),
]
