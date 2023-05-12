# app/main/views.py

# Import django modules & third parties
from django.shortcuts import render

# Import from locals
from app.main import models

# Create your views here.

def home_page(request):
	categories = models.Category.objects.all()
	context = {
		'categories':categories,
	}
	return render(request, 'app/main/index.html', context)
