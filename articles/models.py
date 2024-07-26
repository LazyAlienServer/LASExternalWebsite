from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title = models.CharField(max_length=255, db_default="df_title")
    author = models.CharField(max_length=255, db_default="df_author")
    slug = models.SlugField(max_length=255, unique_for_date='created_at')
    publisher = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    content = CKEditor5Field(config_name='extends')
    pdf_file = models.FileField(upload_to='articles/', db_default='df_pdf')
    original_author_url = models.URLField()
    original_article_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]

    def save(self, *args, **kwargs):
        if not self.publisher_id:
            self.publisher = get_user_model().objects.get(id=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'articles:article_detail',
            kwargs={
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug,
            }
        )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
