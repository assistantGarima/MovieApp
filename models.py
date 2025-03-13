from django.db import models

# Create your models here.

class Moviedata(models.Model):
    title = models.CharField(max_length=1000)
    year = models.IntegerField()
    duration = models.TextField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default="action")
    image = models.ImageField(upload_to="Images/", default = "Images/noimg.jpg")
    
def __str__(self):
    return self.titlle
