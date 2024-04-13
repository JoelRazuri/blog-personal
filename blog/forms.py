from django.forms import ModelForm
from .models import Post
from django import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'titulo', 'class': 'w-full'}),
            'content': forms.Textarea(attrs={'placeholder': 'contenido', 'class': 'w-full h-[100%]'}),
            'image': forms.FileInput(),
        }