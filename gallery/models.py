from django.db import models

# Create your models here.
class Image(models.Model):
  image_url = models.ImageField(upload_to = 'gallery/')
  image_name = models.CharField(max_length=60)
  image_description = models.TextField()

  def __str__(self):
      return self.image_name
  
