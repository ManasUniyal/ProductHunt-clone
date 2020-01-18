from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
import datetime
from django.utils.timezone import utc

def home(request):
    return render(request, 'products/home.html')

@login_required(login_url = 'login')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            product.url = request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.votes_total = 1                  #already has a default value in models.py file
            product.pub_date = datetime.datetime.utcnow().replace(tzinfo=utc)
            product.hunter = request.user
            product.save()
            return redirect('home')
        else:
            return render(request, 'products/create', {'error': 'All fields are compulsory'})
    else:
        return render(request, 'products/create.html')
