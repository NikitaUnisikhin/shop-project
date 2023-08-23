from rest_framework import serializers
from core.apps.accounts.serializers import UserSerializer
from core.apps.catalog.serializers import ProductSerializer
from core.apps.orders.models import OrderItem, Order


class OrderSerializer(serializers.ModelSerializer):
    buyer = UserSerializer()

    class Meta:
        model = Order
        fields = ('buyer', 'order_time', 'delivery_address')


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    seller = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ('order', 'seller', 'product', 'quantity')
