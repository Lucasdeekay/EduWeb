# Generated by Django 3.2.9 on 2021-11-17 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='video',
        ),
    ]
