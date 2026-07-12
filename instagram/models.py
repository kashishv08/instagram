from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    avatar =  models.ImageField(upload_to='avatars')
    bio = models.TextField()
    date_birth = models.DateField()
    followers = models.ManyToManyField(to='self',symmetrical=False, blank=True, related_name='following')
    is_onboard = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user}"


class Post(models.Model):
    likes = models.ManyToManyField(to=User, blank=True, related_name='liked_post')
    attachment =  models.FileField(upload_to='attachments')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    caption = models.TextField()

    def __str__(self):
        return f"{self.user}: {self.caption}"

    def like_counts(self):
        return self.likes.count()

