from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')



class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    # success_url = reverse_lazy('blog:home')



# class LogoutUsuario(LogoutView):
#     next_page = '/blog/'