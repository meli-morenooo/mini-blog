from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Comentario

@receiver(post_save, sender=Post)
def actualizar_numero_entradas(sender, instance, created, **kwargs):
    if created:
        usuario = instance.autor.usuario  # Accede al modelo Usuario a través de la relación OneToOneField
        usuario.numero_entradas += 1
        usuario.save()

@receiver(post_save, sender=Comentario)
def actualizar_numero_comentarios(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.numero_comentarios += 1
        post.save()
