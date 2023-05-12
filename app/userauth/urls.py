from django.urls import path

from app.userauth import views  

app_name = 'userauth'

urlpatterns = [
    path('', views.signup_page, name='signup_page'),
]
