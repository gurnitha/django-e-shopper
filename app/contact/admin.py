# app/contact/admin.py

# Import django modules & third parties
from django.contrib import admin

# Import from locals
from app.contact.models import Contact

# Register your models here.

admin.site.register(Contact)