"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Used to map all the website's routes (Checks here before any other urls.py file)
# Django makes it easy to seperate differnt apps. For ex, if you like a payment page
# that you developed in a seperate app, you can use clever re-routing down below.

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('blog.urls')), 
]
