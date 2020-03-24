# Generated by Django 3.0.4 on 2020-03-24 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artistid',
            field=models.ForeignKey(blank=True, db_column='artistid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='artists.Artist'),
        ),
    ]
