# app/main/models.py

# Import django modules & third parties
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from django import forms  

# Import from locals

# Create your models here.

class UserCreationForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
		label='Email',
		error_messages={'exists':'This email already exists'})

	class Meta:
		model = User 
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user 

	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError(self.fields['email'].error_messages['exists'])
		return self.cleaned_data['email']