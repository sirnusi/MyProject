# Generated by Django 3.0.8 on 2020-07-30 19:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20200728_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('view_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(null=True, upload_to='profilepics'),
        ),
    ]
