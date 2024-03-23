from django.db import models
from datetime import date


class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    image = models.ImageField()
    created_date = models.DateField(default=date.today)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title