# app/main/admin.py

# Import django modules & third parties
from django.contrib import admin

# Import from locals
from app.main.models import Category, Sub_Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)