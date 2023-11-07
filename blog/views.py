from http.client import responses
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Post, Comentario, Usuario
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm
from .serializers import UsuarioSerializer, PostSerializer, ComentarioSerializer, CategoriaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


def lista_posteos(request):
    posts = PostViewSet.as_view({'get': 'list'})(request)
    return render(request, 'blog/lista_posteos.html', {'posts': posts.data})

# @login_required
def nuevo_posteo(request):
    if request.method == "POST":
        form = PostViewSet.as_view({'post': 'create'})(request)
    else:
        form = PostForm()
    return render(request, 'blog/nuevo_posteo.html', {'form': form})

def detalle_posteo(request, pk):
    post = PostViewSet.as_view({'get': 'retrieve'})(request, pk=pk)
    comentarios = Comentario.objects.filter(post=post.data['id'])
    return render(request, 'blog/detalle_posteo.html', {'post': post.data, 'comentarios': comentarios})

# @login_required
def eliminar_posteo(request, pk):
    post = PostViewSet.as_view({'delete': 'destroy'})(request, pk=pk)
    if responses.status_code == status.HTTP_204_NO_CONTENT:
        return redirect('lista_posteos')

# @login_required
def editar_posteo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.autor:
        return redirect('lista_posteos')
    if request.method == "POST":
        form = PostViewSet.as_view({'put': 'update'})(request, pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_posteo.html', {'form': form})

# @login_required
def nuevo_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        data = {
            "texto": request.POST.get("texto"),
            "autor": request.user.id,
            "post": post.id
        }
        serializer = ComentarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('detalle_posteo', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog/nuevo_comentario.html', {'form': form})

# @login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    post_pk = comentario.post.pk
    if request.user == comentario.autor:
        comentario.delete()
    return redirect('detalle_posteo', pk=post_pk)

# @login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.user != comentario.autor:
        return redirect('detalle_posteo', pk=comentario.post.pk)
    if request.method == "POST":
        data = {
            "texto": request.POST.get("texto"),
            "autor": comentario.autor.id,
            "post": comentario.post.id
        }
        serializer = ComentarioSerializer(comentario, data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('detalle_posteo', pk=comentario.post.pk)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'blog/editar_comentario.html', {'form': form})
