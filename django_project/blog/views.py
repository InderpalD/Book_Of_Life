from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

''' We are going to use a list view since our home page
is a list of blogs 
'''

def home(request):
    # Render the home.html file from blog/templates/blog

    template_inputs = {
        'posts': Post.objects.all()
    }

    # By passing additonal args into render, you can access in template file
    return render(request, 'blog/home.html', template_inputs)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

def about(request):
    # Render the about.html file from blog/templates/blog
    return render(request, 'blog/about.html')