# Generated by Django 4.0.5 on 2022-06-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author_post_created_date_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
