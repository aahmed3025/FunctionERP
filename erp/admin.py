from django.contrib import admin

# Register your models here.
from .models import Customer, Supplier, Item, SalesOrder, PurchaseOrder

admin.site.register(Customer)
admin.site.register(Supplier)  
admin.site.register(Item)
admin.site.register(SalesOrder)
admin.site.register(PurchaseOrder)