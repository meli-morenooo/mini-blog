from django.contrib import admin
from .models import Post, Comentario, Categoria, Usuario

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
admin.site.register(Categoria)
admin.site.register(Usuario)
