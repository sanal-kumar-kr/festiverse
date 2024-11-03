# Generated by Django 4.1.4 on 2024-02-15 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('stime', models.TimeField(null=True)),
                ('etime', models.TimeField(null=True)),
                ('buserid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookuserid', to=settings.AUTH_USER_MODEL)),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
    ]