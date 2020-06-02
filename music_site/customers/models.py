from django.db import models

#Customer
class Customer(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    firstname = models.CharField(max_length=40, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    postalcode = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.SET_NULL, blank=True, null=True)
    supportrepid = models.ForeignKey("employees.Employee", on_delete=models.SET_NULL, blank=True, null=True, db_column="supportrepid")

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return "{id} - {firstname} {lastname}".format(
            id = self.id,
            firstname = self.firstname,
            lastname = self.lastname
        )
