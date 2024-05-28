from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    content = forms.FileField(widget=forms.ClearableFileInput())

    class Meta:
        model = Article
        fields = '__all__'

    # def save(self, commit=True):
    #     instance = super(ArticleForm, self).save(commit=False)
    #     upload_file = self.cleaned_data['content']
    #     html = PyDocX.to_html(upload_file)
    #     instance.content = html
    #     instance.save()
    #     return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
