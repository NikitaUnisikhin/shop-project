from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order, OrderItem
from datetime import datetime
from django.http import HttpResponse
from core.apps.cart.cart_extensions import get_user_cart_items, get_user_cart
from .orders_extensions import get_user_orders, get_order_items, get_seller_order_items


@login_required
def add_order(request):
    delivery_address = request.GET.get('delivery_address')  # POST
    cart = get_user_cart(request.user)
    order = Order(buyer=cart.buyer, order_time=datetime.now(), delivery_address=delivery_address)
    order.save()
    cart_items = get_user_cart_items(request.user)
    for item in cart_items:
        OrderItem(order=order, seller=item.product.seller, product=item.product, quantity=item.quantity).save()
        item.delete()
    return HttpResponse('<h4>Заказ оформлен!</h4>')


@login_required
def my_orders(request):
    orders = get_user_orders(request.user)
    orders = dict.fromkeys(orders, list())
    for order in orders.keys():
        orders[order] = get_order_items(order)
    return render(request, 'my_orders.html', {'orders': orders})


@login_required
def clients_orders(request):
    order_items = get_seller_order_items(request.user)
    return render(request, 'clients_orders.html', {'order_items': order_items})
