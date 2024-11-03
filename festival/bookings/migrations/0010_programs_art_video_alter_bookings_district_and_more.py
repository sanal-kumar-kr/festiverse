# Generated by Django 5.0.4 on 2024-06-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_alter_bookings_district'),
        ('decorations', '0005_decfile_decorations_dec_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='art_video',
            field=models.ManyToManyField(to='decorations.decfile'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='district',
            field=models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Ernamkulam', 'Ernamkulam'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kozhikkode', 'Kozhikkode'), ('', 'SELECT'), ('Wayanad', 'Wayanad'), ('Kollam', 'Kollam'), ('Idukki', 'Idukki'), ('Palakkad', 'Palakkad'), ('Pathanamthitta', 'Pathanamthitta'), ('Thrissur', 'Thrissur'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Malappuram', 'Malappuram'), ('Kottayam', 'Kottayam')], default='', max_length=250),
        ),
        migrations.RemoveField(
            model_name='programs',
            name='art_image',
        ),
        migrations.AddField(
            model_name='programs',
            name='art_image',
            field=models.ManyToManyField(to='decorations.file'),
        ),
    ]