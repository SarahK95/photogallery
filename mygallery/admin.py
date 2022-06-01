from django.contrib import admin
from .models import Images,Categorys,Locations

# Register your models here.
admin.site.register(Categorys)
admin.site.register(Images)
admin.site.register(Locations)