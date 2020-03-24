from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserArtist(models.Model):
    userid = models.ForeignKey("auth.User", models.DO_NOTHING, db_column="userid")
    artistid = models.ForeignKey("artists.Artist", models.DO_NOTHING, db_column="artistid")

    class Meta:
        db_table = 'userartist'