from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserAlbum(models.Model):
    userid = models.ForeignKey("auth.User", models.DO_NOTHING, db_column="userid")
    albumid = models.ForeignKey("albums.Album", models.DO_NOTHING, db_column="albumid")

    class Meta:
        db_table = 'useralbum'