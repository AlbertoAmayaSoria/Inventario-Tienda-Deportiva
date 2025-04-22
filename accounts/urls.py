# accounts/urls.py
from django.urls import path
from . import views  # Importa las vistas de la misma app

urlpatterns = [
    path('', views.home, name='home'),  # Redirige a la vista 'home' en la aplicación accounts
]
