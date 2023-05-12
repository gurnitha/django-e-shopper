# app/main/models.py

# Import django modules & third parties
from django.db import models

# Import from locals

# Create your models here.

# MODEL: Category
class Category(models.Model):
	name = models.CharField(max_length=150)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


# MODEL: Sub_Category
class Sub_Category(models.Model):
	name = models.CharField(max_length=150)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Sub category'
		verbose_name_plural = 'Sub categories'

	def __str__(self):
		return self.name


# MODEL: Product
class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=150)
	image = models.ImageField(upload_to='uploads/images/products/')
	price = models.IntegerField()
	date = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.name


