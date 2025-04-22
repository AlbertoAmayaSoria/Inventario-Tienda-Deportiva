# accounts/views.py
from django.shortcuts import render

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')  # Renderiza la plantilla 'home.html'
