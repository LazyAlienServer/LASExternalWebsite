from django.views.generic import (
    ListView, DetailView
)
from django.http import FileResponse, Http404
from rest_framework.views import APIView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleDownloadView(APIView):
    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            file_path = article.pdf_file.path
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=article.pdf_file.name)
        except Article.DoesNotExist:
            raise Http404

