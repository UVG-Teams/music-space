# Generated by Django 3.0.4 on 2020-03-22 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('invoicelineid', models.IntegerField(primary_key=True, serialize=False)),
                ('unitprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('invoiceid', models.ForeignKey(db_column='invoiceid', on_delete=django.db.models.deletion.DO_NOTHING, to='invoices.Invoice')),
            ],
            options={
                'db_table': 'invoiceline',
            },
        ),
    ]