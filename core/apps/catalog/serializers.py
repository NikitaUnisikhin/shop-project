from rest_framework import serializers

from .models import Product
from ..accounts.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer()

    class Meta:
        model = Product
        fields = ('id', 'seller', 'name', 'price', 'description')
