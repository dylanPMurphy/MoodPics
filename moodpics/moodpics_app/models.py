
from django.db import models

from login_reg.models import *
from django.utils import timezone
import math
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

    @property
    def comment_count(self):
        return len(self.comments_on_post.all())
    @property
    def like_count(self):
        return len(self.likers.all())
    @property
    def img_url(self):
        return "https://moodpics.s3-us-west-1.amazonaws.com/media/"+str(self.img)

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"










class Pallette(models.Model):
    
    photo = models.OneToOneField(Post,related_name="pallette",on_delete=models.CASCADE,primary_key=True,)
    color_1 = models.CharField(max_length=10)
    color_2 = models.CharField(max_length=10)
    color_3 = models.CharField(max_length=10)
    color_4 = models.CharField(max_length=10)


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
