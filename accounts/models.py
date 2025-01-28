from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='media_root/profile_images/', default='default_images/perfil.jpg')