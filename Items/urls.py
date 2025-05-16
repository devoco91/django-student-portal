from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.indexPage, name='home'),
    path('post/', views.postPage, name='post'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
]
