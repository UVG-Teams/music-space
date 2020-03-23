from django.db import models

#Genre
class Genre(models.Model):
    genreid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'genre'

    def __str__(self):
        return "{id} - {name}".format(
            id = self.genreid,
            name = self.name
        )
