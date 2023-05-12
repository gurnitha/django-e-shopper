# app/main/views.py

# Import django modules & third parties
from django.shortcuts import render

# Import from locals
from app.main import models

# Create your views here.

def home_page(request):
	categories = models.Category.objects.all()
	products = models.Product.objects.all()

	"""
	Fetching a product that belong to a category and subcategory

	<li><a href="/?category={{category.id}}">{{subcat.name}} </a></li>
	http://127.0.0.1:8000/?category=2	
	"""
	# Step 1: Get category and assign it as category_id
	category_id = request.GET.get('category')

	# Step 2: If there is category_id
	if category_id:
		# Step 2.1: Filter the product where subcategory=category_id and order it by -id
		#         and assign it as products 
		products = models.Product.objects.filter(sub_category=category_id).order_by('-id')

	# Step 3: If Step 1 to 3 not found, return all products
	else:
		products = models.Product.objects.all()

	context = {
		'categories':categories,
		'products':products,
	}
	
	return render(request, 'app/main/index.html', context)
