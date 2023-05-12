from django.urls import path

from app.userauth import views  

app_name = 'userauth'

urlpatterns = [
    path('signup/', views.signup_page, name='signup_page'),
    path('login/', views.signin_page, name='signin_page'),
]
