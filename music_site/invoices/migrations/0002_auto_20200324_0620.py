# Generated by Django 3.0.4 on 2020-03-24 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200324_0620'),
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customerid',
            field=models.ForeignKey(blank=True, db_column='customerid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer'),
        ),
    ]
