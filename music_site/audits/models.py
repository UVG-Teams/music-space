from django.db import models
from django.contrib.auth.models import User

# Audits
class Audit(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    actiontype = models.CharField(max_length=150, blank=False, null=False)
    entity = models.CharField(max_length=100, blank=False, null=False)
    entityid = models.IntegerField(null=True)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_id = models.TextField(max_length=10)
    payload = models.CharField(max_length=500)

    class Meta:
        db_table = 'audit'
