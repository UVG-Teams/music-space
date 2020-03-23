from django.db import models

#Album
class Album(models.Model):
    albumid = models.IntegerField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    artistid = models.ForeignKey("artists.Artist", models.DO_NOTHING, db_column="artistid") #artistid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'album'

    def __str__(self):
        return "{id} - {title}".format(
            id = self.albumid,
            title = self.title
        )
