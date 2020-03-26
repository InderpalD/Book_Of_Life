from django.urls import path
from . import views

# Urls specific to the blog app.
urlpatterns = [
    # The names of these paths are referenced in base.html
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]