from gallery.models import Image
from django.db.models.deletion import SET_NULL
from django.db.models.fields import TextField
from django.test import TestCase

# Create your tests here.
class TestImageClass(TestCase):
  #set up method
  def setUp(self):
      self.new_image = Image(image_url='/gallery/static/images/bmw.jpeg', image_name='BMW coupe', image_description='Red bmw coupe')

  #test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.new_image, Image))