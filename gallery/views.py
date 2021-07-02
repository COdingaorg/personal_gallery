from django.shortcuts import render

# Create your views here.
def index(request):
  title = 'sue gallery'

  return render(request, 'welcome.html', {'title':title})

def gallery_disp(request):
  pass