from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserGenre(models.Model):
    userid = models.ForeignKey("auth.User", on_delete=models.SET_NULL, blank=True, null=True, db_column="userid")
    genreid = models.ForeignKey("genres.Genre", on_delete=models.SET_NULL, blank=True, null=True, db_column="genreid")

    class Meta:
        db_table = 'usergenre'