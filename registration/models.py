from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200, unique=True)
    fee=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.name} (${self.fee})'
    
    
class Student(models.Model):
    SEX_CHOICES=[
        ('M','male'),
        ('F','female'),
        ('Others','others')
        
    ]
    
    
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=200)
    sex=models.CharField(max_length=20, choices=SEX_CHOICES)
    course=models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(upload_to='student')
    date=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.name
    
    
    
class Payment(models.Model):
    PAYMENT_METHODS=[
        ('cash','Cash'),
        ('card','Card'),
        ('transfer','Transfer'),
        ('paystack','Paystck')
    ]
    
    
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    Payment_date=models.DateTimeField(auto_now_add=True)
    Payment_method=models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_reference=models.CharField(max_length=100, unique=True)
    
    
    
    
    def __str__(self):
        return f'{self.student.name} {self.amount}'
