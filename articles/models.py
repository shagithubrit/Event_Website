from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=20)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
     #add in thumbnail
    thumb=models.ImageField(default='default.png',blank=True)
     #add in author later 
    author=models.ForeignKey(User,default=None ,  on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'
       
