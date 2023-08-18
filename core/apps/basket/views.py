from django.shortcuts import render
from django.http import HttpResponse
from .models import BasketItem, Basket
from core.apps.catalog.models import Product


BUYER_ID = 1


# Посмотреть содержимое корзины
def index(request):
    return render(request, 'basket.html',
                  {'items': BasketItem.objects.filter(basket__id=BUYER_ID)})


# Добавить товар в корзину
def add_product(request, product_id):
    BasketItem(
        basket=Basket.objects.filter(buyer__id=BUYER_ID).first(),
        product=Product.objects.get(id=product_id),
        quantity=request.GET.get("quantity", 1)
        ).save()
    return HttpResponse('<h4>Товар добавлен в корзину!</h4>')


# Удалить товар из корзины
def basket_item_delete(request, item_id):
    if request.method == 'GET':
        return HttpResponse()
    elif request.method == 'DELETE':
        BasketItem.objects.get(id=item_id).delete()
        return HttpResponse('<h4>Товар удален!</h4>')
