# Generated by Django 3.0.8 on 2020-09-17 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_auto_20200916_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
    ]
