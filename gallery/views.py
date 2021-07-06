from django.core.mail import message
from django.views.generic import UpdateView, ListView
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Image, Categories, Location, NesletterSubscribers
import datetime as dt
from .forms import NewsletterForm
from .emails import send_welcome_email
from django.contrib.auth.decorators import login_required

# modal window settings
class ModalListView(ListView):
  model = Image
  template_name = 'welcome.html'

  def get_queryset(self):
      return Image.objects.all()

class ModalUpdateView(UpdateView):
  model = Image
  template_name = 'single_img.html'

  def dispatch(self, *args, **kwargs):
    self.id = kwargs['pk']
    return super(ModalUpdateView, self).dispatch(*args, **kwargs)


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
  if 'location' in request.GET and request.GET['location']:
    search_word = request.GET.get('location')
    message = f'Filtered by Location : {search_word}'
    location_images = Image.filter_by_location(search_word)

    return render(request, 'gallery_display.html', {'message':message, 'images':location_images})

  else:

    images = Image.objects.all()
    message = 'Not Filtered'

    categories = Categories.objects.all()
    locations = Location.objects.all()
    return render (request, 'gallery_display.html', {'message':message,'title':title, 'images':images, 'categories':categories, 'locations':locations})

@login_required(login_url='accounts/login')
def single_image(request, image_id):
  try:
    single_image = Image.objects.get(id=image_id)
  except:
    raise Http404('Image Not Available')
  
  return render(request, 'single_img.html', {'single_image': single_image})

def navbar_categories_show(request):
  all_items = Categories.objects.all()

  return render (request,'navbar.html', {'all_items':all_items})

def search_images(request):
  title = 'Category search results'
  if 'category_image' in request.GET and request.GET['category_image']:
    search_term = request.GET.get('category_image')
    message = f'{search_term}'
    result_images = Image.search_by_category(search_term)
    
    categories = Categories.objects.all()

    return render(request, 'search_results.html', {'message':message,'title':title, 'result_images':result_images, 'categories':categories})

  else:
    message = 'You have not searched for anything'
    return render(request, 'search_results.html', {'message':message, 'title':title})

def images_today(request):
  images_today = Image.images_today()
  today = dt.date.today()
  locations = Location.objects.all()

  if request.method == 'POST':
    form = NewsletterForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['user_name']
      email = form.cleaned_data['email']
      recipient = NesletterSubscribers(sub_name = name, email = email)
      recipient.save()
      send_welcome_email(recipient.sub_name,recipient.email)
      message = f'Welcome {name}. Email sent succesfully'
      HttpResponseRedirect('images_today')
    else:
      form = NewsletterForm()
    
    return render(request, 'images_today.html', {'images':images_today, 'today':today, 'locations':locations, 'letterForm':form, 'message':message})
  
  else:
    return render(request, 'images_today.html', {'images':images_today, 'today':today, 'locations':locations})