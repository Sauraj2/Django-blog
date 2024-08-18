from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField()
    slug=models.SlugField()
    date=models.DateTimeField(auto_now_add=True)
    banner=models.ImageField(default='fall.jpg',blank=True)
    
    
    def __str__(self):
        return self.title