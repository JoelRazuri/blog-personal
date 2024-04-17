from django.contrib import admin
from .models import Post, PostView, PostLike


admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(PostLike)

