from django.http.response import Http404
from django.shortcuts import render
from .models import Image, Categories, Location

# Create your views here.
def index(request):
  title = 'sue gallery'
  images = Image.objects.all()[3:9]
  allimages = Image.objects.all()

  image1 = Image.objects.get(pk = 1)
  image2 = Image.objects.get(pk = 2)
  image3 = Image.objects.get(pk = 3)

  return render(request, 'welcome.html', {'title':title, 'images':images, 'allimages':allimages,
  'image1':image1, 'image2':image2, 'image3':image3})

def gallery_disp(request):
  pass

def single_image(request, image_id):
  try:
    single_image = Image.objects.get(id=image_id)
  except:
    raise Http404

  return render(request, 'single_img.html', {'single_image': single_image} )