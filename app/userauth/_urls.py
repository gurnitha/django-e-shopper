from django.urls import path

from app.userauth import views  

app_name = 'userauth'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
]
