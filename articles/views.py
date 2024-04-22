from django.views.generic import (
    TemplateView, ListView, DetailView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


class HomePageView(TemplateView):
    template_name = 'articles/home.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
