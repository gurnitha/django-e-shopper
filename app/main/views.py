# app/main/views.py

# Import django modules & third parties
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

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


@login_required(login_url="/users/login")
def cart_add(request, id):
	cart = Cart(request)
	product = models.Product.objects.get(id=id)
	cart.add(product=product)
	return redirect("main:home_page")


@login_required(login_url="/users/login")
def item_clear(request, id):
	cart = Cart(request)
	product = models.Product.objects.get(id=id)
	cart.remove(product)
	return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
	cart = Cart(request)
	product = models.Product.objects.get(id=id)
	cart.add(product=product)
	return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
	cart = Cart(request)
	product = models.Product.objects.get(id=id)
	cart.decrement(product=product)
	return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
	cart = Cart(request)
	cart.clear()
	return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
	return render(request, 'app/cart/cart_detail.html')