# app/userauth/views.py

# Import django modules & third parties
from django.shortcuts import render

# Import from locals

# Create your views here.

def signup_page(request):
	
	return render(request, 'app/userauth/registration/signup.html')
