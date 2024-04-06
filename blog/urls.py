from django.urls import path
from .views import HomeBlogView, CreatePostView, DetailPostView, UpdatePostView, DeletePostView, Error404View

app_name = 'blog'

urlpatterns = [
    path('', HomeBlogView.as_view(), name='home'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('detail/<int:pk>', DetailPostView.as_view(), name='detail'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('error/', Error404View.as_view(), name='erorr')
]