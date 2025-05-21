from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa las vistas de la app 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para iniciar sesión
    path('logout/', views.logout_view, name='logout'),  # Ruta para cerrar sesión
    path('dashboard/', views.dashboard, name='dashboard'),  # Ruta para el dashboard
    path('register/', views.register_view, name='register'),  # Registro de usuario
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
    path('customer/<str:pk>', views.customer, name='customer'),  # Vista de cliente individual
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),  # Crear orden
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),  # Actualizar orden
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),  # Eliminar orden
    path('panel/', views.panel, name='panel'),  # Panel administrativo

    # 🛒 Rutas para carrito
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrito/', views.cart_view, name='cart_view'),
    path('cart_purchase/', views.cart_purchase, name='cart_purchase'),

    # Página principal
    path('', views.home, name='home')
]
