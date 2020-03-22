from django.db import models

#InvoiceLine
class InvoiceLine(models.Model):
    invoicelineid = models.IntegerField(primary_key=True, blank=False, null=False)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    invoiceid = models.ForeignKey("invoices.Invoice", models.DO_NOTHING, db_column="invoiceid") #invoiceid = models.IntegerField(blank=False, null=False)
    trackid = models.ForeignKey("tracks.Track", models.DO_NOTHING, db_column="trackid") #trackid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'invoiceline'
