from django.contrib import admin
from .models import *

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display=['name','fee']
    list_filter=['name']
    
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','sex','address','phone','course','image','date']
    list_filter=['name','sex','phone','course','date']
class PaymentAdmin(admin.ModelAdmin):
    list_display=['student','amount','Payment_date','payment_reference','Payment_method']
    list_filter=['student','amount','Payment_date']

admin.site.register(Course, CourseAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Payment,PaymentAdmin)

