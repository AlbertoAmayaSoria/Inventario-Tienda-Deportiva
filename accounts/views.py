# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.forms import inlineformset_factory
from accounts.models import *
from .forms import OrderForm


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

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')

    return render(request, 'register.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

#@login_required
#def home(request):
#    return render(request, 'home.html')  # Asegúrate de que esta plantilla esté en 'templates/'

@login_required
def home(request):
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    products = Product.objects.all()

    if category and category != 'All':
        products = products.filter(category=category)
    
    if tag and tag != 'All':
        products = products.filter(tags__name=tag)
    
    if price_min:
        products = products.filter(price__gte=price_min)
    if price_max:
        products = products.filter(price__lte=price_max)

    categories = [c[0] for c in Product.CATEGORY]
    tags = Tag.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

# Dejen esto al ladito por favor

def panel(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Entregado').count()
    pending = orders.filter(status='Pendiente').count()


    context = {'orders':orders, 'customers': customers, 'total_orders': total_orders,
    'delivered': delivered,'pending': pending}

    return render(request, 'panel.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'orders_count':order_count}
    return render(request, 'customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)

        if formset.is_valid():
            formset.save()
            return redirect('/panel/')

    context = {'formset': formset}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)  

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/panel/')


    context = {'form': form}
    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/panel/')
    
    context = {'item': order}
    return render(request, 'delete.html', context)