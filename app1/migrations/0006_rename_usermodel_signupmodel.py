# Generated by Django 4.2 on 2023-09-08 08:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_alter_usermodel_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='SignUpModel',
        ),
    ]
