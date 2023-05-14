# app/order/admin.py

# Import django modules & third parties
from django.contrib import admin

# Import from locals
from app.order.models import Order

# Register your models here.

admin.site.register(Order)