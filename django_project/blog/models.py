from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Define 1-Many relationship


class Post(models.Model):
    '''
    Each post will have a title, content, author, date
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title