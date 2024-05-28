from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Article
import zipfile
import os
import shutil


@receiver(post_save, sender=Article)
def extract_zip_file(sender, instance, created, **kwargs):
    if created:
        file_path = instance.content.path
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            zip_file.extractall(os.path.dirname(file_path))
            macosx_dir = os.path.join(os.path.dirname(file_path), '__MACOSX')
            if os.path.exists(macosx_dir):
                shutil.rmtree(macosx_dir)
        # os.remove(file_path)
