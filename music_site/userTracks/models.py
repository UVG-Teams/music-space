from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserTrack(models.Model):
    userid = models.ForeignKey("auth.User", models.DO_NOTHING, db_column="userid")
    trackid = models.ForeignKey("tracks.Track", models.DO_NOTHING, db_column="trackid")

    class Meta:
        db_table = 'usertrack'