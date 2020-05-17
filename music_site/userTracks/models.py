from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserTrack(models.Model):
    userid = models.ForeignKey("auth.User", on_delete=models.SET_NULL, blank=True, null=True, db_column="userid")
    trackid = models.ForeignKey("tracks.Track", on_delete=models.SET_NULL, blank=True, null=True, db_column="trackid")
    relation = models.CharField(max_length=50, default='uploaded') # uploaded or owned

    class Meta:
        db_table = 'usertrack'