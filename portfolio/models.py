from django.db import models

# Create your models here.
class Profile(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='uploads')
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.firstname
    
    
    
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.CharField(max_length=30)
    image=models.ImageField(upload_to='img')
    date=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.name
