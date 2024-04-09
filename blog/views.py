from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post


class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  
    paginate_by = 8 

    def get_queryset(self):
        return Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['more_views'] = Post.objects.order_by('-id')[:6]
        return context



class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class DetailPostView(DetailView):
    model = Post
    template_name = 'blog/detail_blog.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object.author
        context['more_views'] = Post.objects.order_by('-id')[:6]
        context['related_posts'] = Post.objects.filter(author=author).exclude(pk=self.object.pk).order_by('-id')[:4]
        return context



class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_blog.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:home')



class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:home')


class Error404View(TemplateView):
    template_name = 'layouts/error_404.html'