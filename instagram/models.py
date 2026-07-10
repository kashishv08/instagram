from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    avatar =  models.ImageField(upload_to='avatars')
    bio = models.TextField()
    date_birth = models.DateField()

    def __str__(self):
        return f"{self.user}"

class Post(models.Model):
    attachment =  models.FileField(upload_to='attachments')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    caption = models.TextField()

    def __str__(self):
        return f"{self.user}: {self.caption}"


