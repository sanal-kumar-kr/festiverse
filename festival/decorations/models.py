from django.db import models
from public.models import Register
from django.utils import timezone


class File(models.Model):
    files = models.FileField(null=True) 

class decFile(models.Model):
    files = models.FileField(null=True) 

class decorations(models.Model):
    dec_id = models.ForeignKey(Register, related_name='dec_id', on_delete=models.CASCADE, null=True)
    dec_desc = models.TextField(null=True)
    dec_title=models.CharField(null=True,max_length=250)
    dec_image=models.ManyToManyField(File)
    dec_video=models.ManyToManyField(decFile)
    amount= models.IntegerField(null=True)
    