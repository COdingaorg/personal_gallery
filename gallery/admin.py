from django.contrib import admin
from gallery.models import Image, Location, Categories

class ImageAdmin(admin.ModelAdmin):
  filter_horizontal=('category')
  list_display=('image_name','image-description', 'date_taken', 'location_taken', 'category')
  search_fields = ['category', 'location_taken']
# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Categories)
