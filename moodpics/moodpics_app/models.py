from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.TextField()
    
    img = models.ImageField(upload_to='images/')
