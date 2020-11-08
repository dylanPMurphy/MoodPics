from django.db import models
from login_reg.models import *
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    img = models.ImageField(upload_to='images/')
    poster = models.ForeignKey(User, related_name="posts", on_delete = models.CASCADE)
    likers = models.ManyToManyField(User, related_name="posts_liked")

class Tag(models.Model):
    name = models.CharField(max_length=40)
    photos_tagged = models.ManyToManyField(Post, related_name="post_tags")

class Comment(models.Model):
    comment_content = models.TextField()
    user_who_commented = models.ForeignKey(User, related_name="comments_posted", on_delete = models.CASCADE)
    parent_post = models.ForeignKey(Post, related_name="comments_on_post", on_delete = models.CASCADE)