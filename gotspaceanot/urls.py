from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name = 'gotspaceanot-welcome'),
    path('library_system_records/', views.library_system_records, name = 'gotspaceanot-library_system_records'),
    path('nus_system/', views.nus_system, name = 'gotspaceanot-nus_system'),    
    path('about/', views.about, name='gotspaceanot-about'),
    path('login/', views.login, name = 'gotspaceanot-login'),
    path('logout/', views.logout, name = 'gotspaceanot-logout'),    
    path('library_system/', views.library_system, name = 'gotspaceanot-library_system'),
    path('administrator/', views.administrator, name = 'gotspaceanot-administrator'),
]
