# app/contact/views.py

# Import django modules & third parties
from django.shortcuts import render

# Import from locals

# Create your views here.

def contact_page(request):
	return render(request, 'app/contact/contact.html')
