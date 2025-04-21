from django.contrib import admin
from django.urls import path, include  # Asegúrate de agregar 'include' aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Esta línea incluye tus urls de la app accounts
]

