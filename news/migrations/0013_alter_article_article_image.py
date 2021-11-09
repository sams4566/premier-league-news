# Generated by Django 3.2.9 on 2021-11-09 10:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20211109_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]