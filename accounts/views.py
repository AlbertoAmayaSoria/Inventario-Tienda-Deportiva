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
from django.http import HttpResponseRedirect # para carrito
from django.urls import reverse # para carrito
from .models import Product, Order, Customer #para ordenes


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

    # Todos los productos
    products = Product.objects.all()

    # Productos destacados: siempre los mismos
    featured_products = Product.objects.filter(is_featured=True)

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
        'featured_products': featured_products,  # usados en destacados
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

def contacto(request):
    return render(request, 'contacto.html')

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Obtener o crear carrito en sesión
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart  # Guardar carrito actualizado en sesión
    return HttpResponseRedirect(reverse('home'))

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    products = Product.objects.filter(id__in=cart.keys())

    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })

#@login_required
#def confirm_order(request):
#    if request.method == 'POST':
#        # Aquí podrías guardar la orden en base de datos si lo deseas
#        request.session['cart'] = {}  # Limpiar carrito
#        messages.success(request, 'Orden confirmada exitosamente.')
#        return redirect('home')
#    return redirect('view_cart')

@login_required
def confirm_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Tu carrito está vacío.")
        return redirect('view_cart')

    user = request.user

    # Obtener o crear un Customer vinculado al usuario actual
    customer, created = Customer.objects.get_or_create(
        email=user.email,
        defaults={
            'name': user.username,
            'phone': 'Sin teléfono'
        }
    )

    # Crear una orden por cada producto en el carrito
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        for _ in range(quantity):
            Order.objects.create(
                customer=customer,
                product=product,
                status='Pendiente'
            )

    # Vaciar el carrito
    request.session['cart'] = {}
    messages.success(request, 'Orden registrada exitosamente.')
    return redirect('home')