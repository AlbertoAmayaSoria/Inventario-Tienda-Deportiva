from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verifica las credenciales del usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard si el login es exitoso
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')  # Muestra un mensaje de error si las credenciales son incorrectas

    return render(request, 'login.html')


# Vista del dashboard, solo accesible por usuarios autenticados
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# Vista de bienvenida, solo accesible por usuarios autenticados
@login_required
def home(request):
    return render(request, 'home.html')  # Renderiza la página 'home.html' para usuarios autenticados

