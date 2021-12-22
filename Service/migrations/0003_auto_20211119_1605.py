# Generated by Django 3.2.9 on 2021-11-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_remove_article_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.CharField(max_length=50),
        ),
    ]