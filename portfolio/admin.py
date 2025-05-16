from django.contrib import admin
from .models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','phone','image','address','description','date']
    
    list_filter=['firstname','lastname','address','date']
    
    
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','price','image','date')
    list_filter=('name','price','date')


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Product,ProductAdmin)

