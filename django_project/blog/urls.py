from django.urls import path
from . import views

# Urls specific to the blog app.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]