# Generated by Django 3.0.4 on 2020-06-01 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_track_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='trackid',
            new_name='id',
        ),
    ]
