from django.db import models

#Track
class Track(models.Model):
    trackid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    composer = models.CharField(max_length=220)
    milliseconds = models.IntegerField(blank=False, null=False)
    bytes = models.IntegerField()
    unitprice = models.DecimalField(max_digits=10, decimal_places=2)
    albumid = models.ForeignKey("Album", models.DO_NOTHING, db_column="albumid") #albumid = models.IntegerField()
    genreid = models.ForeignKey("Genre", models.DO_NOTHING, db_column="genreid") #genreid = models.IntegerField()
    mediatypeid = models.ForeignKey("MediaType", models.DO_NOTHING, db_column="mediatypeid") #mediatypeid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'track'
