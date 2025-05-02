# accounts/urls.py
from django.urls import path
from . import views  # Importa las vistas de la app 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para iniciar sesión
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
    path('dashboard/', views.dashboard, name='dashboard'),  # Ruta para el dashboard
    path('register/', views.register_view, name='register'),
    path('', views.home, name='home')
]

