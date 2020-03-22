from django.db import models

# Artist
class Artist(models.Model):
    artistid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'artist'

    # def __str__(self):
    #     return self.name
