from django.db import models

#Customer
class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True, blank=False, null=False)
    firstname = models.CharField(max_length=40, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    company = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60, blank=False, null=False)
    supportrepid = models.ForeignKey("employees.Employee", on_delete=models.SET_NULL, blank=True, null=True, db_column="supportrepid") 
    # FOREIGN KEY (SupportRepId) REFERENCES Employee (EmployeeId) ON DELETE NO ACTION ON UPDATE NO ACTION

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return "{id} - {firstname} {lastname}".format(
            id = self.customerid,
            firstname = self.firstname,
            lastname = self.lastname
        )
