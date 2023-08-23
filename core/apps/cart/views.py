from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem
from core.apps.catalog.models import Product
from .cart_extensions import get_user_cart_items, get_user_cart
from .serializers import CartItemSerializer


@login_required
@api_view(['GET'])
def cart(request):
    queryset = get_user_cart_items(request.user)
    serializer_for_queryset = CartItemSerializer(
        instance=queryset,
        many=True
    )
    return Response(serializer_for_queryset.data)


# Добавить товар в корзину
@login_required
@api_view(['POST'])
def add_product(request):
    product_id = request.data['product_id']
    CartItem(
        cart=get_user_cart(request.user),
        product=Product.objects.get(id=product_id),
        quantity=request.GET.get("quantity", 1)
        ).save()
    return Response('OK')


# Удалить товар из корзины
@login_required
@api_view(['DELETE'])
def delete_cart_item(request):
    CartItem.objects.get(id=request.data['item_id']).delete()
    return Response('OK')
