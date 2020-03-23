from django.db import models

#Employee
class Employee(models.Model):
    employeeid = models.IntegerField(primary_key=True, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    firstname = models.CharField(max_length=20, blank=False, null=False)
    title = models.CharField(max_length=30)
    birthdate = models.DateTimeField()
    hiredate = models.DateTimeField()
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=24)
    fax = models.CharField(max_length=24)
    email = models.CharField(max_length=60)
    reportsto = models.ForeignKey("employees.Employee", models.DO_NOTHING, db_column="reportsto", null=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return "{id} - {firstname} {lastname}".format(
            id = self.employeeid,
            firstname = self.firstname,
            lastname = self.lastname
        )