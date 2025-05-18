"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views
#para imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Accede a las URLs de la app 'accounts'
    path('', views.home, name='home'),  # Ruta raíz para la vista de inicio (home)
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('register/', views.register_view, name='register'),
    path('panel/', views.panel, name='panel') 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

