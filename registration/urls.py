# registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.register_student, name='student'),
    path('start-payment/<int:student_id>/', views.start_payment, name='start_payment'),
    path('payment-webhook/', views.payment_success, name='payment-webhook'),
    path('payment-success/', views.payment_success_page, name='payment-success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
