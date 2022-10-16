from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('terms-condition/', views.terms, name="terms-condition"),
    path('contact/', views.contact, name="contact"),
    path('tour-details/<int:id>/', views.tour_details, name="tour-details"),
]
