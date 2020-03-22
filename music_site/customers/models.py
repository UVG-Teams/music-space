from django.db import models

#Customer
class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True, blank=False, null=False)
    firstname = models.CharField(max_length=40, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    company = models.CharField(max_length=80)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=24)
    fax = models.CharField(max_length=24)
    email = models.CharField(max_length=60, blank=False, null=False)
    supportrepid = models.ForeignKey("Employee", models.DO_NOTHING, db_column="employeeid") # FOREIGN KEY (SupportRepId) REFERENCES Employee (EmployeeId) ON DELETE NO ACTION ON UPDATE NO ACTION

    class Meta:
        db_table = 'customer'
