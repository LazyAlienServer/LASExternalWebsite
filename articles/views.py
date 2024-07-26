from django.views.generic import (
    ListView, DetailView
)
from django.http import FileResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleDownloadView(APIView):
    model = Article

    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        file_path = article.pdf_file.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=article.pdf_file.name)
