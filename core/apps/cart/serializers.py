from rest_framework import serializers
from .models import CartItem, Cart
from ..accounts.serializers import UserSerializer
from ..catalog.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    buyer = UserSerializer()

    class Meta:
        model = Cart
        fields = ('id', 'buyer')


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')
