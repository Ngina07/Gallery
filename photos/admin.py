from django.contrib import admin
from .models import Location,categories,Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(categories)