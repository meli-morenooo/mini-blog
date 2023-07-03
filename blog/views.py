from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm

def lista_posteos(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/lista_posteos.html', {'posts': posts})

@login_required
def nuevo_posteo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posteos')
    else:
        form = PostForm()
    return render(request, 'blog/nuevo_posteo.html', {'form': form})

def detalle_posteo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = Comentario.objects.filter(post=post)
    return render(request, 'blog/detalle_posteo.html', {'post': post, 'comentarios': comentarios})

@login_required
def eliminar_posteo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.autor:
        post.delete()
    return redirect('lista_posteos')

@login_required
def editar_posteo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.autor:
        return redirect('lista_posteos')
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('detalle_posteo', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_posteo.html', {'form': form})

@login_required
def nuevo_comentario(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post
            comentario.save()
            return redirect('detalle_posteo', pk=post.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog/nuevo_comentario.html', {'form': form})

@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    post_pk = comentario.post.pk
    if request.user == comentario.autor:
        comentario.delete()
    return redirect('detalle_posteo', pk=post_pk)

@login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.user != comentario.autor:
        return redirect('detalle_posteo', pk=comentario.post.pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario = form.save()
            return redirect('detalle_posteo', pk=comentario.post.pk)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'blog/editar_comentario.html', {'form': form})
