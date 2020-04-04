from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # Define relationship with the User for our database
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # We are going to override the save function to scale images
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output = (300,300)
            img.thumbnail(output)
            img.save(self.image.path)



