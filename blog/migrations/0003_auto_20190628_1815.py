# Generated by Django 2.0.13 on 2019-06-28 15:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_post_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Posting',
        ),
    ]
