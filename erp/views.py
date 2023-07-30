# erp/views.py

from collections import OrderedDict
from itertools import product
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.test import TestCase

from .models import SalesOrder
from .forms import SalesOrderForm
# Sales Order Create View 
from django.views.generic.edit import CreateView
from .forms import SalesOrderForm

def sales_order_create(request):
    form = SalesOrderForm()
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.id)

    context = {'form': form}
    return render(request, 'sales_order_form.html', context)

# Dashboard View
from django.views.generic import TemplateView

class CustomerDashboard(TemplateView):
    template_name = "customer/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get required data for dashboard       
        context["orders"] = SalesOrder.objects.filter(customer=self.request.user)
        return context

# Sales Order Create View 
from django.views.generic.edit import CreateView
from .forms import SalesOrderForm

class SalesOrderCreateView(CreateView):
    model = SalesOrder
    form_class = SalesOrderForm
    template_name = "sales/order_form.html"
    
    def form_valid(self, form):
        order = form.save(commit=False)
        order.customer = self.request.user
        order.save()
        return super().form_valid(form)
    

# views.py 

# FunctionERP/erp/views.py
from rest_framework.generics import ListCreateAPIView
from .models import Product, Order  # Import the 'Order' model as well
from .serializers import ProductSerializer, OrderSerializer

class ProductListCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderListCreate(ListCreateAPIView):
    queryset = Order.objects.all()  # Use the correct model name 'Order' instead of 'OrderedDict'
    serializer_class = OrderSerializer


from django.urls import reverse

class OrderViewTestCase(TestCase):

    def test_list_orders(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Order List')


# views.py
from django.shortcuts import render

def accounts_view(request):
    # Your view logic here
    # For example:
    return render(request, 'accounts_dashboard.html')

from django.shortcuts import render

def accounts_view(request):
    # Your view logic here
    return render(request, 'accounts_dashboard.html')

# views.py

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')
    







