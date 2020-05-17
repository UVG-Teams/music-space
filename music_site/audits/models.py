from django.db import models
from django.contrib.auth.models import User

# Audits
class Audit(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    action = models.CharField(max_length=150, blank=False, null=False)
    entity = models.CharField(max_length=100, blank=False, null=False)
    entityid = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'audit'
