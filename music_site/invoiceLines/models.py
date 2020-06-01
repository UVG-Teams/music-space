from django.db import models

#InvoiceLine
class InvoiceLine(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    invoice = models.ForeignKey("invoices.Invoice", on_delete=models.SET_NULL, blank=True, null=True, db_column="invoiceid") #invoiceid = models.IntegerField(blank=False, null=False)
    track = models.ForeignKey("tracks.Track", on_delete=models.SET_NULL, blank=True, null=True, db_column="trackid") #trackid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'invoiceline'

    def __str__(self):
        return "{id}".format(
            id = self.invoicelineid
        )
