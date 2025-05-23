from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 

class Product(models.Model):
    CATEGORY = (
        ('Ropa', 'Ropa'),
        ('Calzado', 'Calzado'),
        ('Accesorios', 'Accesorios'),
        ('Equipamiento', 'Equipamiento'),
        ('Tecnología', 'Tecnología'),
        ('Nutrición','Nutrición')
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) #imagenes

    def __str__(self):
        return self.name 


class Order(models.Model):
    STATUS = (
        ('Pendiente', 'Pendiente'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name 