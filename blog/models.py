from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateField(default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title