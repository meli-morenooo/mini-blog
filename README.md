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
