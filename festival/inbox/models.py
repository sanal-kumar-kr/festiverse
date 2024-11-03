from django.db import models
from public.models import Register
from django.utils import timezone




class inbox(models.Model):
    personone = models.ForeignKey(Register, related_name='service_person', on_delete=models.CASCADE, null=True)
    persontwo = models.ForeignKey(Register, related_name='org_id', on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    datetime=models.DateTimeField(null=True)
    status = models.IntegerField(null=True, default=0)
