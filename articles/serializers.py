from rest_framework import serializers

from .models import Article


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = 'pdf_file'
