# Generated by Django 3.2.9 on 2021-11-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20211105_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
