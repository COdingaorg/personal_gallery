from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  url(r'^$', views.index, name = 'home'),
  url(r'^gallery_disp/$', views.gallery_disp, name='gallery_disp'),
  url(r'^search/', views.search_images, name='search_images'),
  url(r'^image/(\d+)/$', views.single_image, name = 'single_image'),
  url(r'^images_today/$', views.images_today, name = 'images_today'),
  url(r'^profile/$', views.profile, name='profile')
]