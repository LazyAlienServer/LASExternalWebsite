# Generated by Django 5.0.4 on 2024-07-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(db_default='df_author', max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='pdf_file',
            field=models.FileField(db_default='df_pdf', upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_default='df_title', max_length=255),
        ),
    ]