# Generated by Django 3.1.5 on 2021-02-03 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chauffuer', '0005_auto_20210203_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_date',
        ),
    ]