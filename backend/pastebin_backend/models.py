from django.db import models
from numpy import empty
import uuid
# Create your models here.
# 具有paste_snap json字段 ip_address字段 
class Paste(models.Model):
    paste_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paste_snap = models.JSONField()
    paste_time = models.DateTimeField(auto_now_add=True)
    expire_time=models.IntegerField()
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    # 具有paste_snap json字段 ip_address字段 
    def __str__(self):
        pass

