from django.db import models

#MediaType
class MediaType(models.Model):
    mediatypeid = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'mediatype'
