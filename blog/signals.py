from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Comentario

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
