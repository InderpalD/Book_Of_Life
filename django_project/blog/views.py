from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    # Render the home.html file from blog/templates/blog

    template_inputs = {
        'posts': Post.objects.all()
    }

    # By passing additonal args into render, you can access in template file
    return render(request, 'blog/home.html', template_inputs)

def about(request):
    # Render the about.html file from blog/templates/blog
    return render(request, 'blog/about.html')