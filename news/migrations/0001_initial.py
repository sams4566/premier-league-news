# Generated by Django 3.2.9 on 2021-11-23 15:03

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
                ('headline', models.CharField(max_length=250)),
                ('extract', models.TextField(max_length=100)),
                ('approved', models.BooleanField(default=False)),
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
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='news.article')),
                ('users_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250)),
                ('approve_category', models.BooleanField(default=False)),
                ('category_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_article', to='news.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='downvote',
            field=models.ManyToManyField(blank=True, related_name='news_downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='upvote',
            field=models.ManyToManyField(blank=True, related_name='news_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
