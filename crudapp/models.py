from django.db import models

# Create your models here.
class customer(models.Model):
    cust_name = models.CharField(max_length=50)
    cust_contact = models.IntegerField()
    cust_city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cust_name}"