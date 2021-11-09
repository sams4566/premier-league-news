# Generated by Django 3.2.9 on 2021-11-08 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_article', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
