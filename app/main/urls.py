from django.urls import path

from app.main import views  

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
