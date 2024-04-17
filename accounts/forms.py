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


class CustomUserUpdateForm(forms.ModelForm):
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña', 'class': 'w-1/2'}),
        required=False,
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir nueva contraseña', 'class': 'w-1/2'}),
        strip=False,
        required=False,
    )
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-1/2'}),
            'last_name': forms.TextInput(attrs={'class': 'w-1/2'}),
            'email': forms.EmailInput(attrs={'class': 'w-1/2'}),
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