from django.contrib import admin
from django.urls import path
import products.views
from django.conf.urls import include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
]
