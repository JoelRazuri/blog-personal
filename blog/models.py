from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from django.db import models
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name='Título')
    content = RichTextField(blank=False, null=False, verbose_name='Contenido')
    image = models.ImageField(upload_to='post_images/', verbose_name='Imagen')
    created_date = models.DateField(default=date.today, verbose_name='Fecha de creación')
    published = models.BooleanField(default=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Autor')

    def __str__(self):
        return self.title
    
    @property
    def get_view_count(self):
        return self.postview_set.all().count()



class PostView(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Autor')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username