# Generated by Django 2.2 on 2019-05-08 05:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventapp', '0014_registered'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registered',
            new_name='Registered1',
        ),
    ]
