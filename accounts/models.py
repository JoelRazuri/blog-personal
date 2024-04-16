from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default='default_images/perfil.jpg')