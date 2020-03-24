from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserPlaylist(models.Model):
    userid = models.ForeignKey("auth.User", on_delete=models.SET_NULL, blank=True, null=True, db_column="userid")
    playlistid = models.ForeignKey("playlists.Playlist", on_delete=models.SET_NULL, blank=True, null=True, db_column="playlistid")

    class Meta:
        db_table = 'userplaylist'