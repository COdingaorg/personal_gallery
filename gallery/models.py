from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
  location_name = models.CharField(max_length=100)

  def __str__(self):
    return self.location_name

  def save_location(self):
    self.save()
  
  def delete_location(self):
    self.delete()

class Categories(models.Model):
  category_name = models.CharField(max_length= 100)

  def __str__(self):
    return self.category_name

  def save_category(self):
    self.save()
  
  def delete_category(self):
    self.delete()

class Image(models.Model):
  image_url = models.ImageField(upload_to = 'gallery/')
  image_name = models.CharField(max_length=60)
  image_description = models.TextField()
  date_taken = models.DateField(default=dt.date.today(), blank=True)
  category = models.ForeignKey(Categories, on_delete=models.CASCADE)
  location_taken = models.ForeignKey(Location, on_delete=models.CASCADE)

  def __str__(self):
      return self.image_name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()
