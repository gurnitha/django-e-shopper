# app/userauth/views.py

# Import django modules & third parties
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 

# Import from locals
from app.userauth import models

# Create your views here.

def signup_page(request):
	if request.method == 'POST':
		form = models.UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
			)

			login(request, new_user)

			return redirect('main:home_page')
	else:
		form = models.UserCreationForm()

	context = {'form':form}
	return render(request, 'app/userauth/registration/signup.html', context)
