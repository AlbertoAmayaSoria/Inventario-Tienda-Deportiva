# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verifica las credenciales del usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')  # Muestra un mensaje de error si las credenciales son incorrectas

    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def home(request):
    return render(request, 'home.html')  # Asegúrate de que esta plantilla esté en 'templates/'

def logout_view(request):
    logout(request)
    return redirect('login')

