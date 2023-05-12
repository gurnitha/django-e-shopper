# app/main/models.py

# Import django modules & third parties
from django.db import models

# Import from locals

# Create your models here.

# MODEL: Category
class Category(models.Model):
	name = models.CharField(max_length=150)


# MODEL: Sub_Category
class Sub_Category(models.Model):
	name = models.CharField(max_length=150)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)





