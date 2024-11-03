from django.db import models
from public.models import Register
from django.utils import timezone
from decorations.models import *
from .models import *

dist={
    ('Thiruvananthapuram','Thiruvananthapuram'),
    ('Kollam','Kollam'),
    ('Pathanamthitta','Pathanamthitta'),
    ('Alappuzha','Alappuzha'),
    ('Kottayam','Kottayam'),
    ('Idukki','Idukki'),
    ('Ernamkulam','Ernamkulam'),
    ('Thrissur','Thrissur'),
    ('Palakkad','Palakkad'),
    ('Malappuram','Malappuram'),
    ('Kozhikkode','Kozhikkode'),
    ('Wayanad','Wayanad'),
    ('Kannur','Kannur'),
    ('Kasaragod','Kasaragod')
}

class programs(models.Model):
    art_id = models.ForeignKey(Register, related_name='art_id', on_delete=models.CASCADE, null=True)
    art_desc = models.TextField(null=True)
    art_title=models.CharField(null=True,max_length=250)
    art_image=models.ManyToManyField(File)
    art_video=models.ManyToManyField(decFile)

    amount= models.IntegerField(null=True)
    
class bookings(models.Model):
    decid = models.ForeignKey(decorations, related_name='bookuserid', on_delete=models.CASCADE, null=True)
    pgid = models.ForeignKey(programs, related_name='bookuserid', on_delete=models.CASCADE, null=True)
    uid = models.ForeignKey(Register, related_name='userid', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    district=models.CharField(default='', max_length=250,choices=dist)
    location=models.CharField(default='', max_length=250)
    stime = models.TimeField(null=True)
    etime = models.TimeField(null=True)
    current_timestamp = timezone.now()
    status=models.IntegerField(null=True,default=0)
    
