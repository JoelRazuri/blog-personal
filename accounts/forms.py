from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'correo electrónico'})
        )
    
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'contraseña'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'repetir contraseña'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'nombre de usuario'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'apellido'}),
        }


class CustomUserUpdateForm(forms.ModelForm):
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}),
        required=False,
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir nueva contraseña'}),
        strip=False,
        required=False,
    )
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'image']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'image': forms.FileInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            self.add_error('new_password2', 'Las contraseñas no coinciden.')
        return cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'nombre de usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'contraseña'
