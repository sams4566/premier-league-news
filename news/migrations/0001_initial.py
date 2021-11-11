# Generated by Django 3.2.9 on 2021-11-10 17:48

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250, unique=True)),
                ('approved', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(default='default_image', max_length=255, verbose_name='image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_article', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('time_created_comment', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='news.article')),
                ('users_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
