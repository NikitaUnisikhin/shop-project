from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html', {'products': Product.objects.all()})


@login_required
def create_product(request):
    if request.method == 'GET':
        return render(request, 'create_product.html')
    elif request.method == 'POST':
        Product(
            seller=request.user,
            name=request.POST.get("name", "Undefined"),
            price=request.POST.get("price", 0),
            description=request.POST.get("description", "Undefined")).save()
        return HttpResponse("<h4>Товар добавлен!</h4>")


def product(request):
    product_id = request.GET.get('product_id')
    if request.method == 'GET':
        return render(request, 'product.html', {'product': Product.objects.get(id=product_id)})
    elif request.method == 'DELETE':
        Product.objects.get(id=product_id).delete()
        return HttpResponse()
