# app/contact/views.py

# Import django modules & third parties
from django.shortcuts import render

# Import from locals
from app.contact import models
# Create your views here.

def contact_page(request):
	
	if request.method == 'POST':
		contact = models.Contact(
			name = request.POST.get('name'),
			email = request.POST.get('email'),
			subject = request.POST.get('subject'),
			message = request.POST.get('message'),
		)

		contact.save()

	return render(request, 'app/contact/contact.html')
