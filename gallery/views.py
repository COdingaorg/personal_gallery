from django.http.response import Http404
from django.shortcuts import render
from .models import Image, Categories, Location

# Create your views here.
def index(request):
  title = 'sue gallery'
  images = Image.objects.all()[3:9]
  allimages = Image.objects.all()

  image1 = Image.objects.get(id = 1)
  image2 = Image.objects.get(id = 2)
  image3 = Image.objects.get(id = 3)

  return render(request, 'welcome.html', {'title':title, 'images':images, 'allimages':allimages,
  'image1':image1, 'image2':image2, 'image3':image3})

def gallery_disp(request):
  title = 'Gallery Display'
  images = Image.objects.all()

  location_images = Image.objects.filter(location_taken=2)
  category_images = Image.objects.filter(category = 3)

  categories = Categories.objects.all()
  locations = Location.objects.all()
  return render (request, 'gallery_display.html', {'title':title, 'images':images, 'location_images':location_images, 
  'category_images':category_images, 'categories':categories, 'locations':locations})

def single_image(request, image_id):
  try:
    single_image = Image.objects.get(id=image_id)
  except:
    raise Http404

  return render(request, 'single_img.html', {'single_image': single_image} )

def navbar_categories_show(request):
  all_items = Categories.objects.all()

  return render (request,'navbar.html', {'all_items':all_items})

def search_images(request):
  title = 'Category search results'
  if 'category_image' in request.GET and request.GET['category_image']:
    search_term = request.GET.get('category_image')
    message = f'{search_term}'
    result_images = Image.search_by_category(search_term)
    
    return render(request, 'search_results.html', {'message':message,'title':title, 'result_images':result_images})

  else:
    message = 'You have not searched for anything'
    return render(request, 'search_results.html', {'message':message, 'title':title})
  