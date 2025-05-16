from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm,CreatePost
from django.contrib.auth import authenticate,login,logout
from django import forms
from .models import *


# Create your views here.

def indexPage(request):
    
    goods=Good.objects.all()
    
    context={'goods':goods}
    return render(request,'items/index.html',context)


def registerPage(request):
    
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
        
    context={'form':form}
    
    return render(request,'items/register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post')  
            messages.info(request, 'Username OR Password is INCORRECT')
    return render(request,'items/login.html')



# from django.shortcuts import render, redirect
# from . import forms  

# def postPage(request):
#     if request.method == 'POST':
#         form = forms.CreatePost(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = forms.CreatePost()  

#     return render(request, 'items/post.html', {'form': form})






def postPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

        if name and price and description:
            post=Good(name=name, price=price, description=description,image=image)
            post.save()
            return redirect('home')
    
    return render(request, 'items/post.html')
