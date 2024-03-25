from django.urls import path
from .views import HomeBlogView, CreateBlogView, DetailBlogView, UpdateBlogView, DeleteBlogView

app_name = 'blog'

urlpatterns = [
    path('', HomeBlogView.as_view(), name='home'),
    path('create/', CreateBlogView.as_view(), name='create'),
    path('detail/<int:pk>', DetailBlogView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateBlogView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteBlogView.as_view(), name='delete'),
]