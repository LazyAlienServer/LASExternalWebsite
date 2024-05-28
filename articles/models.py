from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
import os


class Article(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    content = models.FileField(upload_to='articles/', default='default.html')
    pdf_file = models.FileField(upload_to='articles/', default='default.pdf')
    original_author_url = models.URLField()
    original_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'pk': self.pk})

    def get_file_path(self):
        dir_name = os.path.dirname(self.content.path)
        basename, file_ext = os.path.splitext(os.path.basename(self.content.name))
        basename = basename.replace(" ", "")
        html_filename = f"{basename}.html"
        new_file_path = os.path.join(dir_name, html_filename)
        relative_path = os.path.relpath(new_file_path, settings.MEDIA_ROOT)
        return os.path.join(settings.MEDIA_URL, relative_path)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
