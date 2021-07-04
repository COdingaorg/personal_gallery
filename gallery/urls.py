from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'home'), 
  url(r'^image/(d+)/', views.single_image, name = 'single_image'),
  url(r'^gallery_disp/$', views.gallery_disp, name='gallery_disp'),
 
]