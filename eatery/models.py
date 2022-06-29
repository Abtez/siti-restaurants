from django.db import models
from cloudinary.models import CloudinaryField

class Restaurant(models.Model):
    name = models.CharField(max_length=59, null = True, blank = True)
    image = CloudinaryField('image')
    description = models.TextField(max_length=10009, null = True, blank = True)
    price = models.IntegerField(null = True, blank = True)
    rating = models.IntegerField(null = True, blank = True)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    restaurants = models.ForeignKey(Restaurant, blank=True, null=True, on_delete=models.CASCADE, related_name='restaurant_comments')
    comments = models.CharField(max_length=59, null = True, blank = True)
    likes = models.IntegerField(null = True, blank = True)
    
    def __str__(self):
        return self.restaurants.name
    


