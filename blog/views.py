from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# home page
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<post>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(ListView):
    model = Post

# about page
def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})