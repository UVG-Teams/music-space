from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class UserGenre(models.Model):
    userid = models.ForeignKey("auth.User", models.DO_NOTHING, db_column="userid")
    genreid = models.ForeignKey("genres.Genre", models.DO_NOTHING, db_column="genreid")

    class Meta:
        db_table = 'usergenre'