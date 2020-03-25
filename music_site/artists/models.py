from django.db import models

# Artist
class Artist(models.Model):
    artistid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'artist'

    def __str__(self):
        return "{id} - {name}".format(
            id = self.artistid,
            name = self.name
        )
