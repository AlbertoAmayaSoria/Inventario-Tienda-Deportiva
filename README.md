# 🏪 Inventario-Tienda-Deportiva

Sistema web ficticio que permite consultar el inventario de una tienda deportiva. Cualquier persona puede acceder a la visualización de productos, pero solo los empleados autorizados pueden realizar compras o modificar el inventario.

---

## 👥 INTEGRANTES DEL EQUIPO

- David Casanova  
- Juan Pablo Zurita  
- Angel Alberto Amaya  
- Orlando Pacheco  
- Andres Gutierrez  

---

## ⚙ INSTRUCCIONES DE USO

### 1. Clonar el repositorio

```bash
git clone https://github.com/AlbertoAmayaSoria/Inventario-Tienda-Deportiva.git
cd Inventario-Tienda-Deportiva
```

### 2. Crear entorno virtual con Pipenv

```bash
pipenv install
pipenv shell
```

### 3. Aplicar migraciones y correr el servidor

```bash
python manage.py migrate
python manage.py runserver
```

Abre tu navegador en:  
🔗 http://127.0.0.1:8000/

### 4. Crear un superusuario para el panel de administración

```bash
python manage.py createsuperuser
```

Luego accede al panel admin en:  
🔗 http://127.0.0.1:8000/admin/

---

## 📌 FUNCIONALIDADES IMPLEMENTADAS

| Funcionalidad                                 | Estado | Observaciones                                       |
|-----------------------------------------------|--------|----------------------------------------------------|
| Visualización de productos por visitantes      | ✔      | Vista `products()` muestra productos disponibles   |
| Filtro por categoría, precio y etiquetas       | ✔      | Soportado mediante campos de modelo                |
| Carga de imágenes para productos               | ✔      | El modelo contiene `ImageField`                   |
| Gestión CRUD desde panel de administrador      | ✔      | Admin de Django habilitado                         |
| Autenticación de usuarios                      | ✔      | Login, logout y registro implementados             |
| Roles diferenciados: cliente / empleado        | ✔      | A definir                                          |
| Registro de pedidos                            | ✔      | Vista `panel()` muestra órdenes por estado         |
| Historial o bitácora de acciones               | ❌     | No implementado por el momento                     |
| Agregar productos al carrito                   | ✔      | Botón "Añadir al carrito" disponible               |
| Eliminar productos del carrito                 | ✔      | Opción de "Eliminar" en el carrito implementada    |

---

## 🧱 MODELOS UTILIZADOS

### `Product`
- `name`: nombre del producto
- `price`: precio
- `category`: categoría (con opciones predefinidas)
- `description`: descripción
- `date_created`: fecha de creación automática
- `tags`: etiquetas relacionadas (many-to-many)
- `image`: imagen del producto

### `Order`
- `customer`: relación con el cliente
- `product`: producto relacionado
- `date_created`: fecha de creación automática
- `status`: estado del pedido (Pendiente, En camino, Entregado)

### `Customer`
- `name`: nombre del cliente
- `phone`: teléfono
- `email`: correo electrónico
- `date_created`: fecha de registro

---

## 🌐 VISTAS Y RUTAS

| URL                        | Vista             | Descripción                                     |
|----------------------------|-------------------|-------------------------------------------------|
| `/`                        | `home`            | Página de inicio                                |
| `/login/`                  | `login_view`      | Iniciar sesión                                  |
| `/logout/`                 | `logout_view`     | Cerrar sesión                                   |
| `/register/`               | `register_view`   | Registro de usuario                             |
| `/dashboard/`              | `dashboard`       | Dashboard de usuario                            |
| `/panel/`                  | `panel`           | Panel resumen de órdenes y clientes             |
| `/products/`               | `products`        | Vista con todos los productos disponibles       |
| `/customer/<str:pk>`       | `customer`        | Vista de información de clientes                |
| `/add-to-cart/<int:id>/`   | `add_to_cart`     | Agregar producto al carrito                     |
| `/cart/`                   | `cart_view`       | Vista del carrito de compras                    |
| `/remove-from-cart/<int:id>/` | `remove_from_cart` | Eliminar producto del carrito             |

---

## 🖼️ GESTIÓN DE IMÁGENES

Las imágenes se deben guardar en la carpeta:  
📁 `media/product_images/`

Asegúrate de tener esta configuración en `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Y en `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧪 PRUEBAS

Para ejecutar las pruebas (si se agregan):

```bash
python manage.py test
```

---

## 📦 DEPENDENCIAS REQUERIDAS

Asegúrate de instalar las siguientes dependencias antes de ejecutar el proyecto:

```bash
pipenv install django
pipenv install pillow
```

---

## ⚠️ NOTAS FINALES

- Este proyecto es educativo y no está conectado a un sistema real de ventas.
- Se recomienda iniciar sesión como superusuario para acceder al panel completo.
- Las imágenes se guardan localmente.
