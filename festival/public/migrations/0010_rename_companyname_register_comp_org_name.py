# Generated by Django 5.0.2 on 2024-02-20 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0009_register_companyname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='companyname',
            new_name='comp_org_name',
        ),
    ]
