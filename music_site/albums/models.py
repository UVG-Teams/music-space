from django.db import models

#Album
class Album(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    artistid = models.ForeignKey("artists.Artist", on_delete=models.SET_NULL, blank=True, null=True, db_column="artistid")

    class Meta:
        db_table = 'album'

    def __str__(self):
        return "{id} - {title}".format(
            id = self.id,
            title = self.title
        )
