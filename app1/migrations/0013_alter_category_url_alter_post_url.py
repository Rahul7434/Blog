# Generated by Django 4.2 on 2023-09-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_category_url_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
    ]
