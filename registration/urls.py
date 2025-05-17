from django.urls import path 
from . import views

urlpatterns = [
    path('student/',views.register_student, name='student'),
    path('start-payment/<int:student_id>/', views.start_payment, name='start_payment'),
    
    path('dashboard/',views.dashboard, name='dashboard'),
    
    
]
