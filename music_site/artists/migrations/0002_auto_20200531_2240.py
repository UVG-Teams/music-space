# Generated by Django 3.0.4 on 2020-05-31 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='artistid',
            new_name='id',
        ),
    ]
