from django.db import models

#Playlist
class Playlist(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'playlist'

    def __str__(self):
        return "{id} - {name}".format(
            id = self.id,
            name = self.name
        )
