from django.db import models

#PlaylistTrack
class PlaylistTrack(models.Model):
    playlistid = models.ForeignKey("playlists.Playlist", models.DO_NOTHING, db_column="playlistid") #playlistid = models.IntegerField(primary_key=True, blank=False, null=False)
    trackid = models.ForeignKey("tracks.Track", models.DO_NOTHING, db_column="trackid") #trackid = models.IntegerField(primary_key=True, blank=False, null=False)

    class Meta:
        db_table = 'playlisttrack'
