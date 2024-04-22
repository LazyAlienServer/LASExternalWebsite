from django import forms
from ckeditor.fields import RichTextFormField

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    content = RichTextFormField(config_name='default')

    class Meta:
        model = Article
        fields = ['content', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
