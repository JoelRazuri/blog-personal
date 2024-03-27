from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')



class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    next_page = 'blog:home'



class LogoutUserView(LogoutView):
    next_page = 'blog:home'