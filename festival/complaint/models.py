from django.db import models
from public.models import Register
from .models import*
from django.utils import timezone




class complaint(models.Model):
    userid = models.ForeignKey(Register, related_name='cuid', on_delete=models.CASCADE, null=True)
    dec_art_id = models.ForeignKey(Register, related_name='dec_art_id', on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=250,null=True)
    complaint = models.TextField(null=True)
    response = models.TextField(null=True)
    datetime=models.DateTimeField(null=True)
    status = models.IntegerField(null=True, default=0)
