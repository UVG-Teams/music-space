from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserPlaylist(models.Model):
    userid = models.ForeignKey("auth.User", models.DO_NOTHING, db_column="userid")
    playlistid = models.ForeignKey("playlists.Playlist", models.DO_NOTHING, db_column="playlistid")

    class Meta:
        db_table = 'userplaylist'