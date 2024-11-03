# Generated by Django 5.0.2 on 2024-02-17 18:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('stime', models.TimeField(null=True)),
                ('etime', models.TimeField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('org_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_id', to=settings.AUTH_USER_MODEL)),
                ('service_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]