from django import forms
from django.forms import TextInput, Textarea, Select
from .models import Post, Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'contenido', 'categorias')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)

        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
        }
