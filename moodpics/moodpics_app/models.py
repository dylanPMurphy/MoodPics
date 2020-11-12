from django.db import models
from login_reg.models import *

# Create your models here.

MOOD_CHOICES = [
        ("B", "Brilliant"),
        ("G", "Gloom"),
        ("L","Lush"),
        ("V","Vibrant"),
        ("M","Mystique"),
        ("T","Turbulant"),
]


class Post(models.Model):
    title = models.CharField(max_length=40)
    img = models.FileField()
    poster = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    likers = models.ManyToManyField(User, related_name="posts_liked")
    mood = models.CharField(max_length=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pallette(models.Model):
    
    photo = models.OneToOneField(Post,on_delete=models.CASCADE,primary_key=True,)
    color_1 = models.CharField(max_length=6)
    color_2 = models.CharField(max_length=6)
    color_3 = models.CharField(max_length=6)
    color_4 = models.CharField(max_length=6)
    color_5 = models.CharField(max_length=6)


class Tag(models.Model):
    name = models.CharField(max_length=40)
    photos_tagged = models.ManyToManyField(Post, related_name="post_tags")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_content = models.TextField()
    user_who_commented = models.ForeignKey(User, related_name="comments_posted", on_delete = models.CASCADE)
    parent_post = models.ForeignKey(Post, related_name="comments_on_post", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)