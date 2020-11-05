from django.shortcuts import render
from .models import Post

# home page
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# about page
def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})