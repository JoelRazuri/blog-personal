from django.shortcuts import redirect


def blog_home(request):
    return redirect('blog:home')