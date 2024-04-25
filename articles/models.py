from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    content = models.FileField(upload_to='articles/%Y/%m/%d/')
    original_author_url = models.URLField()
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
