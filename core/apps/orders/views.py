from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.apps.basket.models import Basket, BasketItem
from .models import Order, OrderItem
from datetime import datetime
from django.http import HttpResponse


@login_required
def add(request):
    delivery_address = request.GET.get('delivery_address')  # POST
    basket = Basket.objects.filter(buyer__id=request.user.id).first()
    order = Order(buyer=basket.buyer, order_time=datetime.now(), delivery_address=delivery_address)
    order.save()
    basket_items = BasketItem.objects.filter(basket_id=basket.id)
    for item in basket_items:
        OrderItem(order=order, seller=item.product.seller, product=item.product, quantity=item.quantity).save()
        item.delete()
    return HttpResponse('<h4>Заказ оформлен!</h4>')


@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer__id=request.user.id)
    orders = dict.fromkeys(orders, list())
    for order in orders.keys():
        orders[order] = OrderItem.objects.filter(order__id=order.id)
    return render(request, 'my_orders.html', {'orders': orders})


@login_required
def clients_orders(request):
    order_items = OrderItem.objects.filter(seller__id=request.user.id)
    print(len(order_items))
    return render(request, 'client_orders.html', {'order_items': order_items})
