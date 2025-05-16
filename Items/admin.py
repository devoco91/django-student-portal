from django.contrib import admin

from .models import *

# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display=('name','description','price','image','date')
    list_filter=('name','price','date')


admin.site.register(Good,GoodAdmin)


