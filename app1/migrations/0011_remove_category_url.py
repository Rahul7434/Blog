# Generated by Django 4.2 on 2023-09-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_remove_post_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]
