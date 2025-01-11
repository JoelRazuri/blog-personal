from django.db.models.base import Model as Model
from django.db.models import Count
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from accounts.forms import CustomUserUpdateForm
from accounts.models import CustomUser
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .forms import PostForm
from .models import Post, PostView
from django.http import HttpResponseRedirect


class HomeBlogView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'  
    paginate_by = 4 

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
        context['more_views'] = Post.objects.filter(published=True).annotate(view_count=Count('postview')).order_by('-view_count')[:6]
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
        messages.success(self.request, '¡La publicación se ha creado correctamente! Espere a que el administrador la habilite')
        form.instance.author = self.request.user
        return super().form_valid(form)



class DetailPostView(DetailView):
    model = Post
    template_name = 'blog/detail_blog.html'
    context_object_name = 'post'

    def get_object(self, **kwargs):
        post = super().get_object(**kwargs)
        PostView.objects.create(post=post)
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object.author
        context['more_views'] = Post.objects.filter(published=True).annotate(view_count=Count('postview')).order_by('-view_count')[:6]
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
        changes_made = False
        new_image = self.request.FILES.get('image')
        if new_image:
            changes_made = True
        if not changes_made:
            for field in form.changed_data:
                if field != 'image':  
                    changes_made = True
                    break
        if not changes_made:
            messages.info(self.request, '¡No hizo ningún cambio!')
            return self.redirect_to_success()
        user = form.save(commit=False)
        if new_image:
            user.image = new_image 
        user.save()
        messages.success(self.request, '¡Tus datos de perfil se han actualizado correctamente!')
        return super().form_valid(form)

    def redirect_to_success(self):
        return HttpResponseRedirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, '¡Hubo un error al actualizar tus datos de perfil. Por favor, inténtalo de nuevo!')
        return super().form_invalid(form)


class ProfileListPostsView(ListView):
    model = Post
    template_name = 'blog/profile_list_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-id')