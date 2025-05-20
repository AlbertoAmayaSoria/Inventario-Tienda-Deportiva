# accounts/urls.py
from django.urls import path
from . import views  # Importa las vistas de la app 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para iniciar sesión
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
    path('dashboard/', views.dashboard, name='dashboard'),  # Ruta para el dashboard
    path('register/', views.register_view, name='register'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
    path('panel/', views.panel, name='panel'),
    path('', views.home, name='home')
]

