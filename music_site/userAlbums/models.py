from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserAlbum(models.Model):
    userid = models.ForeignKey("auth.User", on_delete=models.SET_NULL, blank=True, null=True, db_column="userid")
    albumid = models.ForeignKey("albums.Album", on_delete=models.SET_NULL, blank=True, null=True, db_column="albumid")

    class Meta:
        db_table = 'useralbum'