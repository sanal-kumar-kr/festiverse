# Generated by Django 5.0.2 on 2024-02-17 19:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_remove_events_amount_remove_events_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='events',
            new_name='inbox',
        ),
    ]
