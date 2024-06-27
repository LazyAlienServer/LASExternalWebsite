# Generated by Django 5.0.4 on 2024-06-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_slug_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pdf_file',
            field=models.FileField(db_default='default.pdf', upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(db_default='default-slug', max_length=255, unique=True),
        ),
    ]