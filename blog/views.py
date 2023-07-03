from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def lista_posteos(request):
    posts = Post.objects.all()
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

@login_required
def eliminar_posteo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.autor:
        post.delete()
    return redirect('lista_posteos')
