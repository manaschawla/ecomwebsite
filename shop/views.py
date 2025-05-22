from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
import json
from .models import Product,Contact,Order,OrderUpdate

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
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, desc = desc, phone = phone)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')



def search(request):
    return render(request, 'shop/search.html')

def products(request, myid):
    #fetch the product using id
    product = Product.objects.filter(id = myid)
    return render(request, 'shop/prodview.html', {'product': product[0]})

def checkout(request):
        if request.method == "POST":
            items_json= request.POST.get('itemsJson', '')
            name = request.POST.get('name', '')
            email = request.POST.get('inputEmail4', '')
            phone = request.POST.get('inputPhone', '')
            address = request.POST.get('inputAddress','')
            address2 = request.POST.get('inputAddress2','')
            state = request.POST.get('inputState','')
            zip = request.POST.get('inputZip','')
            city = request.POST.get('inputCity','')
            orders = Order(items_json = items_json, name = name, email = email, address = address, address2 = address2, phone = phone , state = state, city = city , zip_code = zip)
            orders.save()
            update = OrderUpdate(order_id = orders.order_id, update_desc = "the order has been placed")
            update.save()
            thank=True
            id=orders.order_id
            return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
        return render(request, 'shop/checkout.html')