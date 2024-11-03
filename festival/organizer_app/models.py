from django.db import models
from public.models import Register
from django.utils import timezone


class events(models.Model):
    eventname=models.CharField(max_length=50,default='')
    eventdescription=models.TextField(null=True)
    buserid = models.ForeignKey(Register, related_name='eventartistuserid', on_delete=models.CASCADE, null=True)
    uid = models.ForeignKey(Register, related_name='userbookingid', on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    stime = models.TimeField(null=True)
    etime = models.TimeField(null=True)
    current_timestamp = timezone.now()
    amount=models.IntegerField(null=True)
    status=models.IntegerField(null=True,default=0)
# Create your models here.
