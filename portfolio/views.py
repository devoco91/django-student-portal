from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'portfolio/flowerabay.html',context)
