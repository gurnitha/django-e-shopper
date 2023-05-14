# app/contact/models.py

# Import django modules & third parties
from django.db import models

# Import from locals

# Create your models here.

# MODEL: Contact
class Contact(models.Model):
	name = models.CharField(max_length=150)
	email = models.EmailField(max_length=150)
	subject = models.CharField(max_length=150)
	message = models.TextField()

	class Meta:
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return self.name