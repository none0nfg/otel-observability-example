from django.contrib import admin
from django.urls import path, include
from secpath import views

urlpatterns = [
    path('', views.main),
    path('d/<str:rand>', views.link),
]
