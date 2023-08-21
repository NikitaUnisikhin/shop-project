from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import CartItem
from core.apps.catalog.models import Product
from .cart_extensions import get_user_cart_items, get_user_cart


# Посмотреть содержимое корзины
@login_required
def index(request):
    return render(request, 'cart.html', {'items': get_user_cart_items(request.user)})


# Добавить товар в корзину
@login_required
def add_product(request):
    product_id = request.GET.get('product_id')
    CartItem(
        cart=get_user_cart(request.user),
        product=Product.objects.get(id=product_id),
        quantity=request.GET.get("quantity", 1)
        ).save()
    return HttpResponse('<h4>Товар добавлен в корзину!</h4>')


# Удалить товар из корзины
@login_required
def delete_cart_item(request, item_id):
    if request.method == 'GET':
        return HttpResponse()
    elif request.method == 'DELETE':
        CartItem.objects.get(id=item_id).delete()
        return HttpResponse('<h4>Товар удален!</h4>')
