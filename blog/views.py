from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'



class CreateBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('blog:home')



class DetailBlogView(DetailView):
    model = Post
    template_name = 'blog/detail_blog.html'
    context_object_name = 'post'



class UpdateBlogView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_blog.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:home')



class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog:home')
    
