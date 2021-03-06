# Generated by Django 3.0.8 on 2020-08-27 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0008_auto_20200825_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='like_count',
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='article_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
