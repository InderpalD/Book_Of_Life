from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Inderpal',
        'title': 'Post 1',
        'content': 'First Post!',
        'date_posted': 'March 25, 2020'
    },

    {
        'author': 'Paul',
        'title': 'Post 2',
        'content': 'Second Post!',
        'date_posted': 'March 25, 2020'
    }

]

def home(request):
    # Render the home.html file from blog/templates/blog

    template_inputs = {
        'posts': posts,
        'title': 'yo'
    }

    # By passing additonal args into render, you can access in template file
    return render(request, 'blog/home.html', template_inputs)

def about(request):
    # Render the about.html file from blog/templates/blog
    return render(request, 'blog/about.html')