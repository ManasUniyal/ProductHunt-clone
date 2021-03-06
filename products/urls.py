from django.contrib import admin
from django.urls import path
import products.views
from django.conf.urls import include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_id>/', views.details, name='details'),
    path('<int:product_id>/upvote/', views.upvote, name='upvote'),
    path('search/', views.search, name='search'),
]
