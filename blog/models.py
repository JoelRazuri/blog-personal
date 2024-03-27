from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name='Título')
    content = models.TextField(blank=False, null=False, verbose_name='Contenido')
    image = models.ImageField(upload_to='post_images/' ,verbose_name='Imagen')
    created_date = models.DateField(default=date.today, verbose_name='Fecha de creación')
    author = models.ForeignKey(User, on_delete=models.CASCADE,erbose_name='Autor')

    def __str__(self):
        return self.title