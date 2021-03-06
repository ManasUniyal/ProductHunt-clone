from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Vote
import datetime
from django.utils.timezone import utc
from django.shortcuts import get_object_or_404

def home(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products':products})

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
            vote = Vote()
            vote.product = product
            vote.user = request.user
            vote.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create', {'error': 'All fields are compulsory'})
    else:
        return render(request, 'products/create.html')

def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/details.html', {'product':product})

@login_required(login_url = 'login')
def upvote(request, product_id):
    if request.method == 'POST':
        votes = Vote.objects.all()
        flag = True
        for vote in votes:
            if vote.user == request.user and vote.product.id == product_id:
                flag = False
                break
        if flag:
            product = get_object_or_404(Product, id=product_id)
            product.votes_total += 1
            product.save()
            vote = Vote()
            vote.user = request.user
            vote.product = product
            vote.save()
    return redirect('/products/'+str(product_id))

def search(request):
    search_result_list = list()
    if request.method == 'POST':
        products = Product.objects.all()
        for product in products:
            if request.POST['search'].lower() in product.title.lower():
                search_result_list.append(product)
        return render(request, 'products/home.html', {'products': search_result_list})
