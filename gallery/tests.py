from gallery.models import Image, Location
from django.db.models.deletion import SET_NULL
from django.db.models.fields import TextField
from django.test import TestCase

# Create your tests here.
class TestLocation(TestCase):
  #setup method
  def setUp(self):
    self.new_location = Location(location_name = 'Kibra')

  #test instance
  def test_instance_creation(self):
    self.assertTrue(isinstance(self.new_location, Location))
  
  #test save method
  def test_save_location(self):
    self.new_location.save_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)
