# Generated by Django 3.1.5 on 2021-02-02 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chauffuer', '0002_auto_20210201_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_author',
        ),
    ]
