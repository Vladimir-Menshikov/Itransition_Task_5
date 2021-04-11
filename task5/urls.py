from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
]
