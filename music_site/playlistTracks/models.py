from django.db import models

#PlaylistTrack
class PlaylistTrack(models.Model):
    playlistid = models.ForeignKey("playlists.Playlist", on_delete=models.CASCADE, db_column="playlistid") #playlistid = models.IntegerField(primary_key=True, blank=False, null=False)
    trackid = models.ForeignKey("tracks.Track", on_delete=models.CASCADE, db_column="trackid") #trackid = models.IntegerField(primary_key=True, blank=False, null=False)

    class Meta:
        db_table = 'playlisttrack'

    def __str__(self):
        return "{id} - {trackid}".format(
            id = self.playlistid,
            trackid = self.trackid
        )
