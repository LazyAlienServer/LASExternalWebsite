from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    content = forms.FileField(widget=forms.ClearableFileInput())

    class Meta:
        model = Article
        fields = ['content', ]

    def clean_content(self):
        file = self.cleaned_data.get('content')
        if file.name.endswith('.pdf'):
            raise ValidationError(
                _('Please select a PDF file'),
                code='invalid_file_type',
            )
        return file


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
