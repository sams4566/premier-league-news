# Generated by Django 3.2.9 on 2021-11-09 11:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_rename_article_image_article_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='Image'),
            preserve_default=False,
        ),
    ]