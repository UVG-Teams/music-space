# Generated by Django 3.0.4 on 2020-03-24 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artists', '0001_initial'),
        ('userArtists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userartist',
            name='artistid',
            field=models.ForeignKey(blank=True, db_column='artistid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='artists.Artist'),
        ),
        migrations.AlterField(
            model_name='userartist',
            name='userid',
            field=models.ForeignKey(blank=True, db_column='userid', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
