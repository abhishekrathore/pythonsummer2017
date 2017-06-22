from django.db import models

# Create your models here.

class Post(models.Model):
     content = models.TextField(null=False)
     user = models.ForeignKey('User',on_delete=models.CASCADE)
     title = models.CharField(max_length=512,null=False)
     published_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,null=False)
    url = models.URLField()


    def __str__(self):
        return self.username

class Comment(models.Model):
    content = models.TextField(null=False)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

