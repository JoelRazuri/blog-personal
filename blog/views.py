from django.shortcuts import render
from django.views.generic import View



class BlogHomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blog/index.html',{})
