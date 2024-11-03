# Generated by Django 5.0.4 on 2024-07-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0010_programs_art_video_alter_bookings_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='district',
            field=models.CharField(choices=[('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Thrissur', 'Thrissur'), ('Kollam', 'Kollam'), ('Wayanad', 'Wayanad'), ('Ernamkulam', 'Ernamkulam'), ('Pathanamthitta', 'Pathanamthitta'), ('Kasaragod', 'Kasaragod'), ('Malappuram', 'Malappuram'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Palakkad', 'Palakkad'), ('Idukki', 'Idukki'), ('Kozhikkode', 'Kozhikkode'), ('Kannur', 'Kannur')], default='', max_length=250),
        ),
    ]