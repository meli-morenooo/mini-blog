from django.test import TestCase
from .models import Post, Categoria, Comentario

class PostModelTest(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Categoria de prueba')
        self.post = Post.objects.create(titulo='Post de prueba', contenido='Contenido de prueba')
        self.post.categorias.add(self.categoria)
        self.comentario = Comentario.objects.create(texto='Comentario de prueba', post=self.post)

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.titulo, 'Post de prueba')
        self.assertEqual(post.contenido, 'Contenido de prueba')
        self.assertIn(self.categoria, post.categorias.all())
    
    def test_comentario_creation(self):
        comentario = Comentario.objects.get(id=1)
        self.assertEqual(comentario.texto, 'Comentario de prueba')
        self.assertEqual(comentario.post, self.post)
