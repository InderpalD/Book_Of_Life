from django.urls import path
from . import views
from .views import PostListView, PostDetailView

# Urls specific to the blog app.
urlpatterns = [
    # The names of these paths are referenced in base.html
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]


