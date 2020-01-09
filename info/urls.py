from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('blue', views.blue, name= 'blue'),
    path('about', views.about, name='about' ),
    path('refresh', views.refresh, name='refresh'),  
    path('attendance', views.attendance, name='attendance'), 
    path('student_table', views.student_table, name='student_table'),
    path('records', views.records, name='records'),   
] 
