from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product

def index(request):
    products = Product.objects.all()
    print(products)
    print("Total products:", len(products))
    #params = {'no_of_slides': nSlides , 'range': range(nSlides) ,'product' :  products}
    #allprods = [[products, range(1, nSlides), nSlides],
        #       [products, range(1, nSlides), nSlides]]
    allprods = []
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        n = len(products)
        nSlides = nSlides = ceil(n / 4)
        prod = Product.objects.filter(category = cat)
        allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params )


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/index.html')

def tracker(request):
    return render(request, 'shop/index.html')

def search(request):
    return render(request, 'shop/index.html')

def prodview(request):
    return render(request, 'shop/index.html')

def checkout(request):
    return HttpResponse("hello")