from django.db import models

#Invoice
class Invoice(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    invoicedate = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    billingaddress = models.CharField(max_length=70, null=True)
    billingcity = models.CharField(max_length=40, null=True)
    billingstate = models.CharField(max_length=40, blank=True, null=True)
    billingcountry = models.CharField(max_length=40, null=True)
    billingpostalcode = models.CharField(max_length=10, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey("customers.Customer", on_delete=models.SET_NULL, blank=True, null=True, db_column='customerid')

    class Meta:
        db_table = 'invoice'

    def __str__(self):
        return "{id}".format(
            id = self.invoiceid,
        )
