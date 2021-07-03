from gallery.models import Categories, Image, Location
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
  
  #test update method
  def test_update_location(self):
    self.new_location.save_location()
    locations = Location.objects.filter(location_name = 'Kibra')
    locations.update(location_name = 'Manyatta')

    self.new_location.refresh_from_db()

    self.assertEqual(self.new_location.location_name, 'Manyatta')

  def test_delete_location(self):
    self.new_location.save_location()
    self.new_location.delete_location()
    locations = Location.objects.all()
    self.assertTrue(len(locations)==0)

class TestCategories(TestCase):
  #setup method
  def setUp(self):
    self.new_category = Categories(category_name = 'E-bikes')

  #test instance
  def test_instance_creation(self):
    self.assertTrue(isinstance(self.new_category, Categories))
  
  #test save method
  def test_save_category(self):
    self.new_category.save_category()
    categories = Categories.objects.all()
    self.assertTrue(len(categories)>0)
  
  #test update method
  def test_update_category(self):
    self.new_category.save_category()
    categories = Categories.objects.filter(category_name = 'E-bikes')
    categories.update(category_name = 'Nature')

    self.new_category.refresh_from_db()

    self.assertEqual(self.new_category.category_name, 'Nature')

  def test_delete_category(self):
    self.new_category.save_category()
    self.new_category.delete_category()
    categories = Categories.objects.all()
    self.assertTrue(len(categories)==0)

class TestImageClass(TestCase):
  #set up instance
  def setUp(self):
    self.new_location = Location(location_name = 'Kibra')
    self.new_location.save()

    self.new_category = Categories(category_name = 'E-bikes')
    self.new_category.save()

    self.new_image = Image(image_url = '/gallery/static/images/bmw.jpeg',image_name = 'BMW red Coupe',image_description = 'Red Coupe BMW model 2020', location_taken = self.new_location, category = self.new_category)


  #test instance
  def test_instance_created(self):
    self.assertTrue(isinstance(self.new_image, Image))

  #save image
  def test_save_image(self):
    self.new_image.save_image()

    images = Image.objects.all()

    self.assertTrue(len(images)>0)

  def test_delete_method(self):
    self.new_image.save_image()

    self.new_image.delete_image()

    images = Image.objects.all()
    self.assertTrue(len(images)==0)

  def test_update_method(self):
    self.new_image.save_image()

    images = Image.objects.filter(image_name = 'BMW red Coupe')

    images.update(image_name = 'Red BMW')
    self.new_image.refresh_from_db()

    self.assertEqual(self.new_image.image_name, 'Red BMW')