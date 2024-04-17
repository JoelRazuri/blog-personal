from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from accounts.forms import CustomUserUpdateForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q
from .forms import PostForm
from .models import Post

class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  
    paginate_by = 8 

    def get_queryset(self):
        queryset = Post.objects.filter(published=True).order_by('-id')
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(author__username__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['more_views'] = Post.objects.filter(published=True).order_by('-id')[:6]
        return context



class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('blog:profile_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def form_valid(self, form):
        messages.success(self.request, '¡La publicación se ha creado correctamente!')
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
    success_url = reverse_lazy('blog:profile_posts')

    def form_valid(self, form):
        messages.success(self.request, '¡La publicación se ha actualizado correctamente!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al actualizar la publicación. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)



class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:profile_posts')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '¡La publicación se ha eliminado correctamente!')
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class Error404View(TemplateView):
    template_name = 'layouts/error_404.html'



class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'blog/profile_user_update.html'
    context_object_name = 'user'
    success_url = reverse_lazy('blog:profile')

    def dispatch(self, request, *args, **kwargs):
       self.object = self.get_object()
       return super().dispatch(request, *args, **kwargs)
    
    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.image = self.request.FILES.get('image')
        user.save()
        messages.success(self.request, '¡Tus datos de perfil se han actualizado correctamente!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al actualizar tus datos de perfil. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)

class ProfileListPostsView(ListView):
    model = Post
    template_name = 'blog/profile_list_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-id')