from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=100)

  def __str__(self):
      return self.location_name

class Categories(models.Model):
  category_name = models.CharField(max_length= 100)

  def __str__(self):
    return self.category_name

class Image(models.Model):
  image_url = models.ImageField(upload_to = 'gallery/')
  image_name = models.CharField(max_length=60)
  image_description = models.TextField()
  date_taken = models.DateField(default=dt.date.today())
  category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
  location_taken = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)

  def __str__(self):
      return self.image_name






  
