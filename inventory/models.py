from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
