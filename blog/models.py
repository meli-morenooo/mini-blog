from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    numero_comentarios = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentario por {self.autor.username} en {self.post.titulo}'


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_entradas = models.IntegerField(default=0)

@receiver(post_save, sender=Post)
def actualizar_numero_entradas(sender, instance, created, **kwargs):
    if created:
        instance.autor.usuario.numero_entradas += 1
        instance.autor.usuario.save()

@receiver(post_save, sender=Comentario)
def actualizar_numero_comentarios(sender, instance, created, **kwargs):
    if created:
        instance.post.numero_comentarios += 1
        instance.post.save()
