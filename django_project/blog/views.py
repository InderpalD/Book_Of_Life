from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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


# For home page posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


# For User page posts
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # Override query function
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Override this function to link author to post during submit post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Override this function to link author to post during submit post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Run by UserPassesTestMixin and used to check if person updating post is author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Define where to send user after deleting post

    # Run by UserPassesTestMixin and used to check if person deleting post is author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    # Render the about.html file from blog/templates/blog
    return render(request, 'blog/about.html')