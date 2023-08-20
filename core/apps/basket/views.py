from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import BasketItem, Basket
from core.apps.catalog.models import Product


# Посмотреть содержимое корзины
@login_required
def index(request):
    return render(request, 'basket.html',
                  {'items': BasketItem.objects.filter(
                      basket=Basket.objects.filter(buyer__id=request.user.id).first())})


# Добавить товар в корзину
@login_required
def add_product(request, product_id):
    buyer = request.user
    basket = Basket.objects.get_or_create(buyer=buyer)[0]
    BasketItem(
        basket=basket,
        product=Product.objects.get(id=product_id),
        quantity=request.GET.get("quantity", 1)
        ).save()
    return HttpResponse('<h4>Товар добавлен в корзину!</h4>')


# Удалить товар из корзины
@login_required
def basket_item_delete(request, item_id):
    if request.method == 'GET':
        return HttpResponse()
    elif request.method == 'DELETE':
        BasketItem.objects.get(id=item_id).delete()
        return HttpResponse('<h4>Товар удален!</h4>')
