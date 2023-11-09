# Mini Blog en Django

Este es un proyecto de un blog básico hecho en Django.

## Prerrequisitos

Antes de poder ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.6 o superior
- Pip (gestor de paquetes de Python)
- Virtualenv (herramienta para crear entornos virtuales de Python)

## Instrucciones de instalación y ejecución

1. **Descarga el proyecto**

   Puedes clonar este proyecto usando git. Para eso, ejecuta el siguiente comando en tu terminal:

   ```
   git clone URL_DEL_REPOSITORIO
   ```

   **Nota:** Debes reemplazar `URL_DEL_REPOSITORIO` con la URL de este repositorio en GitHub.

2. **Crea un entorno virtual y actívalo**

   Navega hasta el directorio del proyecto (donde se encuentra el archivo `manage.py`) y ejecuta los siguientes comandos para crear y activar el entorno virtual:

   - En Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instala las dependencias**

   Una vez activado el entorno virtual, instala las dependencias del proyecto con el siguiente comando:

   ```
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones de la base de datos**

   Django usa un sistema de migraciones para manejar la base de datos. Ejecuta el siguiente comando para aplicar las migraciones:

   ```
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional)**

   Si quieres acceder a la interfaz de administración de Django, necesitarás un superusuario. Para crearlo, ejecuta el siguiente comando y sigue las instrucciones:

   ```
   python manage.py createsuperuser
   ```
   
   En el caso de utilizar el archivo db.sqlite3 del proyecto, el usuario y contraseña son los siguientes:
   - username: admin
   - password: admin

6. **Ejecuta el servidor de desarrollo**

   Finalmente, puedes ejecutar el servidor de desarrollo de Django con el siguiente comando:

   ```
   python manage.py runserver
   ```

   Ahora deberías poder ver el proyecto en tu navegador accediendo a `http://localhost:8000`.

## Características del proyecto

Este proyecto de blog en Django incluye las siguientes características:

- Posteos de blog con autores, fechas y contenido.
- Comentarios en los posteos.
- Vista de detalle para cada posteo con sus comentarios correspondientes.
- Interfaz de administración para gestionar posteos y comentarios.
- Creación, edición y eliminación de posteos y comentarios.

## Pruebas

Este proyecto utiliza Pytest para realizar pruebas. Puedes ejecutar las pruebas con el siguiente comando:

```bash
pytest
```

Aquí hay un ejemplo de una prueba que crea una nueva categoría y comprueba si se guardó correctamente:

```python
import pytest
from .models import Categoria

# este decorador es para que lo teste pero no afecte a la base de datos
@pytest.mark.django_db
def test_get_categoria():
    nueva_categoria = Categoria.objects.create(
        nombre = 'categoria de test',
    )

    categoria = Categoria.objects.all()

    assert categoria.count() == 1
    assert categoria[0].nombre == nueva_categoria.nombre
```

Y aquí hay otro ejemplo de una prueba que crea varias categorías y comprueba que se hayan creado correctamente:

```python
@pytest.mark.django_db
def test_get_categorias():
    for x in range(20):
         nueva_categoria = Categoria.objects.create(
            nombre = 'otro test',
    )

    categoria = Categoria.objects.all()

    assert categoria.count() == 20
    assert categoria[0].nombre == 'Terror'
```

Para ejecutar un test específico, puedes usar la opción `-k` de pytest seguida del nombre de la función de prueba. Por ejemplo, para ejecutar solo `test_get_categoria`, puedes utilizar el siguiente comando:

```bash
pytest -k test_get_categoria
```

# 
# NUEVAS FUNCIONALIDADES: Mini Blog API

#### 1. API para el Miniblog

Se ha implementado una API robusta utilizando `ModelViewSet` para gestionar las operaciones CRUD en los modelos clave del Miniblog:

- **Usuario:** Permite realizar operaciones en la entidad de Usuario.
- **Entrada (Post):** Habilita la manipulación de las entradas del blog.
- **Comentario:** Ofrece operaciones CRUD para gestionar comentarios en las entradas.
- **Categoría:** Proporciona endpoints para administrar las categorías de las entradas.

Además, se ha documentado detalladamente la API en el README. La documentación incluye información sobre los endpoints disponibles, los métodos permitidos (GET, POST, PUT, DELETE), así como ejemplos concretos de las solicitudes y respuestas esperadas. Esta documentación facilita la comprensión y el uso de la API para desarrolladores externos.

La API ha sido probada y verificada su accesibilidad desde herramientas como Postman y una extension de VSCode llamada Thunder Client, garantizando el correcto funcionamiento.

#### 2. Autenticación en la API

Se ha implementado un sistema de autenticación en la API utilizando Django Rest Framework. Esta implementación asegura que solo los usuarios autenticados tengan la capacidad de realizar acciones sensibles, como crear, actualizar o eliminar sus propias entradas y comentarios. Esto mejora la seguridad y la privacidad al restringir ciertas operaciones a usuarios autorizados.

#### 3. Tests Adicionales

Se han agregado pruebas adicionales utilizando pytest para cubrir las nuevas funcionalidades y la lógica de la API. Estas pruebas incluyen casos para verificar el acceso protegido y  la correcta autenticación de usuarios. Estos tests garantizan que las nuevas funcionalidades funcionan según lo previsto.

## Endpoints de la API

### Usuarios
- Listar usuarios: `GET /api/usuarios/`
- Detalle de usuario: `GET /api/usuarios/<id>/`
- Crear usuario: `POST /api/usuarios/`
- Actualizar usuario: `PUT /api/usuarios/<id>/`
- Eliminar usuario: `DELETE /api/usuarios/<id>/`

### Posts
- Listar posts: `GET /api/posts/`
- Detalle de post: `GET /api/posts/<id>/`
- Crear post: `POST /api/posts/`
- Actualizar post: `PUT /api/posts/<id>/`
- Eliminar post: `DELETE /api/posts/<id>/`

### Comentarios
- Listar comentarios: `GET /api/comentarios/`
- Detalle de comentario: `GET /api/comentarios/<id>/`
- Crear comentario: `POST /api/comentarios/`
- Actualizar comentario: `PUT /api/comentarios/<id>/`
- Eliminar comentario: `DELETE /api/comentarios/<id>/`

### Categorías
- Listar categorías: `GET /api/categorias/`
- Detalle de categoría: `GET /api/categorias/<id>/`
- Crear categoría: `POST /api/categorias/`
- Actualizar categoría: `PUT /api/categorias/<id>/`
- Eliminar categoría: `DELETE /api/categorias/<id>/`


## Pruebas API

El proyecto incluye pruebas automatizadas para garantizar el correcto funcionamiento de las API. Las pruebas se encuentran en el archivo `test_api.py` y se pueden ejecutar utilizando `pytest`. Asegúrate de seguir los siguientes pasos para ejecutar las pruebas:

```bash
# Activar el entorno virtual (si lo estás utilizando)
source venv/bin/activate  # En Linux/macOS
.\venv\Scripts\Activate  # En Windows (PowerShell)

# Instalar las dependencias
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Configurar la base de datos (si es necesario)
python manage.py migrate

# Ejecutar las pruebas de API
pytest -k test_access_protected_views  # Ejecutar solo las pruebas de acceso protegido
pytest -k test_access_unauthorized_views  # Ejecutar solo las pruebas de acceso no autorizado
```

### Descripción de las Pruebas

- **Acceso Protegido:** Las pruebas en `test_access_protected_views` aseguran que las vistas protegidas devuelvan respuestas exitosas cuando se accede con un cliente autenticado.

- **Acceso No Autorizado:** Las pruebas en `test_access_unauthorized_views` garantizan que las vistas protegidas devuelvan códigos de estado 401 cuando se accede sin autenticación.
