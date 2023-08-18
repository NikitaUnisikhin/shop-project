from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Seller


def index(request):
    return render(request, 'basket.html', {'products': Product.objects.all()})


def creating_product(request):
    if request.method == 'GET':
        return render(request, 'create_product.html')
    elif request.method == 'POST':
        Product(
            seller=Seller.objects.get(id=1),
            name=request.POST.get("name", "Undefined"),
            price=request.POST.get("price", 0),
            description=request.POST.get("description", "Undefined")).save()
        return HttpResponse("<h4>Товар добавлен!</h4>")


def product(request, product_id):
    if request.method == 'GET':
        return render(request, 'product.html', {'product': Product.objects.get(id=product_id)})
    elif request.method == 'DELETE':
        Product.objects.get(id=product_id).delete()
        return HttpResponse()
