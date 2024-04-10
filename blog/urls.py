from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import handler404
from .views import (
    HomeBlogView, 
    CreatePostView, 
    DetailPostView, 
    UpdatePostView, 
    DeletePostView, 
    UserUpdateView,
    Error404View
    )

app_name = 'blog'

handler404 = Error404View.as_view()

urlpatterns = [
    path('', HomeBlogView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('detail/<int:pk>', DetailPostView.as_view(), name='detail'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('profile/<int:pk>', login_required(UserUpdateView.as_view()), name='profile'),
]
