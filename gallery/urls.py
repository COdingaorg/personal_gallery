from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^gallery_disp/$', views.gallery_disp, name='gallery_disp'),
  url(r'^image/(d+)', views.single_image, name = 'single_image')
]