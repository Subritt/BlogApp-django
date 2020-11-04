from django.shortcuts import render
from django.http import HttpResponse

# home page
def home(request):
    return render(request, 'blog/home.html')

# about page
def about(request):
    return render(request, 'blog/about.html')