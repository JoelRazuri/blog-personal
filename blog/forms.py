from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'titulo'}),
            'content': forms.TextInput(attrs={'placeholder': 'contenido'}),
        }