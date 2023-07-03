"""
URL configuration for miniblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_posteos, name='lista_posteos'),
    path('post/nuevo/', views.nuevo_posteo, name='nuevo_posteo'),
    path('post/<int:pk>/editar/', views.editar_posteo, name='editar_posteo'),
    path('post/<int:pk>/', views.detalle_posteo, name='detalle_posteo'),
    path('post/<int:pk>/eliminar/', views.eliminar_posteo, name='eliminar_posteo'),
    path('post/<int:pk>/comentario/nuevo/', views.nuevo_comentario, name='nuevo_comentario'),
    path('comentario/<int:pk>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:pk>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),

]
