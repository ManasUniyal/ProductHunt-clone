from django.contrib import admin

# Register your models here.

from .models import Product, Vote

admin.site.register(Product)
admin.site.register(Vote)
