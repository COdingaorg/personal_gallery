from django.contrib import admin
from gallery.models import Image, Location, Categories

class ImageAdmin(admin.ModelAdmin):
  filter_horizontal=('category')
# Register your models here.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Categories)
