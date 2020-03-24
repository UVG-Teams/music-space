from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserArtist(models.Model):
    userid = models.ForeignKey("auth.User", on_delete=models.SET_NULL, blank=True, null=True, db_column="userid")
    artistid = models.ForeignKey("artists.Artist", on_delete=models.SET_NULL, blank=True, null=True, db_column="artistid")

    class Meta:
        db_table = 'userartist'