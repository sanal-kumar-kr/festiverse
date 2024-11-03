from django.db import models
from public.models import Register
from django.utils import timezone


class feedback(models.Model):
    fuserid = models.ForeignKey(Register, related_name='fid', on_delete=models.CASCADE, null=True)
    uid = models.ForeignKey(Register, related_name='uid', on_delete=models.CASCADE, null=True)
    feedbackmsg = models.TextField(null=True)
    current_timestamp = timezone.now()
    ratings = models.IntegerField(null=True)
