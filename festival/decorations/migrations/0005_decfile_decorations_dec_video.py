# Generated by Django 5.0.4 on 2024-06-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decorations', '0004_file_remove_decorations_dec_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='decFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='decorations',
            name='dec_video',
            field=models.ManyToManyField(to='decorations.decfile'),
        ),
    ]