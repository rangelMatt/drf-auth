# Generated by Django 4.0.3 on 2022-05-31 21:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sounds', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drf',
            new_name='Sound',
        ),
    ]
