from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'correo electrónico', 'class': 'w-1/2'})
        )
    
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'contraseña', 'class': 'w-1/2'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'repetir contraseña', 'class': 'w-1/2'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'nombre de usuario', 'class': 'w-1/2'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'nombre', 'class': 'w-1/2'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'apellido', 'class': 'w-1/2'}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'nombre de usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'contraseña'