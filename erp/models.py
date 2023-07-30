from collections import OrderedDict
from multiprocessing import context
from django.db import models
from requests import request

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
        
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Sales Order #{self.id} for {self.customer}"

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Purchase Order #{self.id} for {self.supplier}"
    

from django.db.models import JSONField

class SalesOrder(models.Model):
    details = JSONField()



from django.db import models

class SalesOrder(models.Model):
    # Your model fields and definitions here
    # For example:
    order_number = models.CharField(max_length=20)
    order_date = models.DateField()
    # Add other fields as needed

# FunctionERP/erp/models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

class SalesOrder(models.Model):
    # Add the status and customer fields here
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Add other fields as needed


# FunctionERP/erp/models.py
from django.db import models

class Product(models.Model):
    # Your Product model fields and definitions here
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    date_added = models.DateTimeField('date added')

class Order(models.Model):
    # Your Order model fields and definitions here
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        )









