from django.db import models

#Track
class Track(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    composer = models.CharField(max_length=220, blank=True, null=True)
    milliseconds = models.IntegerField(blank=False, null=False)
    bytes = models.IntegerField()
    unitprice = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    albumid = models.ForeignKey("albums.Album", on_delete=models.SET_NULL, blank=True, null=True, db_column="albumid") #albumid = models.IntegerField()
    genreid = models.ForeignKey("genres.Genre", on_delete=models.SET_NULL, blank=True, null=True, db_column="genreid") #genreid = models.IntegerField()
    mediatypeid = models.ForeignKey("mediaTypes.MediaType", on_delete=models.SET_NULL, blank=True, null=True, db_column="mediatypeid") #mediatypeid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'track'

    def __str__(self):
        return "{id} - {name}".format(
            id = self.id,
            name = self.name
        )
