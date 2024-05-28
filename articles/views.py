from django.views.generic import (
    TemplateView, ListView, DetailView
)
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.http import FileResponse, Http404
from rest_framework.views import APIView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['file_path'] = article.get_file_path()
        return context


class ArticleDownloadView(APIView):
    def get(self, request, pk, format=None):
        try:
            article = Article.objects.get(pk=pk)
            file_path = article.pdf_file.path
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=article.pdf_file.name)
        except Article.DoesNotExist:
            raise Http404

