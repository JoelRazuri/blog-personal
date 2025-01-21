from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import handler404
from .views import (
    HomeBlogView, 
    CreatePostView, 
    DetailPostView, 
    UpdatePostView, 
    DeletePostView, 
    ProfileUpdateView,
    ProfileListPostsView,
    Error404View
    )

app_name = 'blog'

handler404 = Error404View.as_view()

urlpatterns = [
    path('', HomeBlogView.as_view(), name='home'),
    path('detail/<int:pk>', DetailPostView.as_view(), name='detail'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('profile/', login_required(ProfileUpdateView.as_view()), name='profile'),
    path('profile/posts', login_required(ProfileListPostsView.as_view()), name='profile_posts'),
    path('profile/create/post', login_required(CreatePostView.as_view()), name='create'),
    path('profile/update/post/<int:pk>', login_required(UpdatePostView.as_view()), name='update'),
]
