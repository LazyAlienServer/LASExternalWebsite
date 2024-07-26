from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'slug',
            'author',
            'content',
            'pdf_file',
            'original_author_url',
            'original_article_url',
        )
        widgets = {
            'content': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
