from django.db import models

#Invoice
class Invoice(models.Model):
    invoiceid = models.IntegerField(primary_key=True, blank=False, null=False)
    invoicedate = models.DateTimeField(blank=False, null=False)
    billingaddress = models.CharField(max_length=70)
    billingcity = models.CharField(max_length=40)
    billingstate = models.CharField(max_length=40)
    billingcountry = models.CharField(max_length=40)
    billingpostalcode = models.CharField(max_length=10)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    customerid = models.ForeignKey("Customer", models.DO_NOTHING, db_column="customerid") #customerid = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'invoice'