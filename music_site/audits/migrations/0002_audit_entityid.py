# Generated by Django 3.0.4 on 2020-05-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='entityId',
            field=models.IntegerField(null=True),
        ),
    ]
