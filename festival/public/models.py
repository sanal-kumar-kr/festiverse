from django.db import models

from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
    gender = models.CharField(max_length=50,null=True)
    specialskills = models.TextField(max_length=500,default='')
    dob=models.CharField(max_length=50,default='')
    contact = models.IntegerField(null=True)
    address = models.TextField(null=True)
    usertype = models.IntegerField(null=True)
    status=models.IntegerField(null=True,default=0)
    amount=models.IntegerField(null=True)
    profile=models.FileField(null=True)
    idproof=models.FileField(null=True)
    previousworks=models.FileField(null=True)
    amountperhour=models.IntegerField(null=True)
    comp_org_name=models.CharField(max_length=500,default='')
    experience=models.TextField(null=True)
    street=models.CharField(max_length=50,default='')
    city=models.CharField(max_length=50,default='')
    pin=models.IntegerField(null=True)
    pr_type=models.CharField(max_length=50,default='')
    interest=models.IntegerField(null=True)


    