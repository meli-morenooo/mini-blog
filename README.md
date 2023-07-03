## Paso a paso para la creación del proyecto "miniblog"

Este repositorio de GitHub contiene los pasos necesarios para crear el proyecto "miniblog" utilizando Django. A continuación, se detalla el proceso paso a paso para configurar y ejecutar el proyecto.

### Requisitos previos
Asegúrate de tener instalado Python y pip en tu sistema antes de continuar. También necesitarás tener `virtualenv` instalado. Si no lo tienes, puedes instalarlo utilizando el siguiente comando:

```shell
pip install virtualenv
```

### Configuración del entorno virtual

1. Clona este repositorio en tu máquina local:

```shell
git clone https://github.com/TU_USUARIO/miniblog.git
```

2. Navega hasta la carpeta del proyecto:

```shell
cd miniblog
```

3. Crea un entorno virtual e inícialo:

```shell
virtualenv venv
source venv/bin/activate
```

### Instalación de dependencias

1. Asegúrate de que estás dentro del entorno virtual (el prefijo `(venv)` debe aparecer en tu línea de comandos).

2. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`:

```shell
pip install -r requirements.txt
```

### Configuración de Django

1. Genera la configuración inicial de Django ejecutando el siguiente comando:

```shell
django-admin startproject miniblog .
```

2. Realiza las migraciones necesarias para configurar la base de datos:

```shell
python manage.py migrate
```

### Ejecución del servidor de desarrollo

1. Verifica que la configuración se haya realizado correctamente ejecutando el servidor de desarrollo de Django:

```shell
python manage.py runserver
```

2. Abre tu navegador web e ingresa la URL `http://localhost:8000/` para acceder al proyecto "miniblog".

### Creación de la aplicación "blog"

1. Crea una nueva aplicación llamada "blog" utilizando el siguiente comando:

```shell
python manage.py startapp blog
```

2. Continuar....
