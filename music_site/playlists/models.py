from django.db import models

#Playlist
class Playlist(models.Model):
    playlistid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'playlist'
