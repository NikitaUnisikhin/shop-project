from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order, OrderItem
from datetime import datetime
from core.apps.cart.cart_extensions import get_user_cart_items, get_user_cart
from .orders_extensions import get_user_orders, get_seller_order_items, get_order_items
from .serializers import OrderSerializer, OrderItemSerializer


@login_required
@api_view(['POST'])
def add_order(request):
    delivery_address = request.data['delivery_address']
    cart = get_user_cart(request.user)
    order = Order(buyer=cart.buyer, order_time=datetime.now(), delivery_address=delivery_address)
    order.save()
    cart_items = get_user_cart_items(request.user)
    for item in cart_items:
        OrderItem(order=order, seller=item.product.seller, product=item.product, quantity=item.quantity).save()
        item.delete()
    return Response('OK')


@login_required
@api_view(['GET'])
def my_orders(request):
    queryset = get_user_orders(request.user)
    serializer_for_queryset = OrderSerializer(
        instance=queryset,
        many=True
    )
    return Response(serializer_for_queryset.data)


@login_required
@api_view(['GET'])
def clients_orders(request):
    queryset = get_seller_order_items(request.user)
    serializer_for_queryset = OrderItemSerializer(
        instance=queryset,
        many=True
    )
    return Response(serializer_for_queryset.data)
