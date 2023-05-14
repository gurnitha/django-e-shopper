from django.urls import path

from app.contact import views  

app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact_page, name='contact_page'),
]
