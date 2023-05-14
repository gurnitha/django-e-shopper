# app/order/models.py

# Import django modules & third parties
from django.db import models
from django.contrib.auth.models import User 
import datetime 

# Import from locals
from app.main.models import Product  

# Create your models here.

# MODEL: Order
class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='uploads/order/images/')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity = models.CharField(max_length=5)
	price = models.IntegerField()
	address = models.TextField()
	phone = models.CharField(max_length=15)
	pincode = models.CharField(max_length=10)
	date = models.DateField(default=datetime.datetime.today)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Orders'

	def __str__(self):
		return self.product.name
