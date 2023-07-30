from django import forms
from .models import SalesOrder, PurchaseOrder 

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'status']

class PurchaseOrderForm(forms.ModelForm):  
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'status']

from django.test import Client, TestCase

class OrderFormTestCase(TestCase):

    def test_valid_data(self):
        client = Client()
        data = {'product': 'Table', 'amount': 300}
        response = client.post('/orders/create/', data)
        self.assertEqual(response.status_code, 302)
    
    def test_invalid_data(self):
        client = Client()
        data = {'product': ''}
        response = client.post('/orders/create/', data)
        self.assertContains(response, 'This field is required')


# FunctionERP/erp/forms.py
from django import forms
from .models import SalesOrder

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = '__all__'
