from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainapp, name='mainapp'),
    path('scrap/', views.scrap, name='scrap'),
    path('display/', views.display, name='display')
]

