from django.db import models

#MediaType
class MediaType(models.Model):
    mediatypeid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'mediatype'

    def __str__(self):
        return "{id} - {name}".format(
            id = self.mediatypeid,
            name = self.name
        )
