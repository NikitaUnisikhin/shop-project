from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response


@api_view(['GET'])
def products(request):
    queryset = Product.objects.all()
    serializer_for_queryset = ProductSerializer(
        instance=queryset,
        many=True
    )
    return Response(serializer_for_queryset.data)

@api_view(['GET'])
def product_by_id(request, id):
    queryset = Product.objects.get(id=id)
    serializer_for_queryset = ProductSerializer(
        instance=queryset,
    )
    return Response(serializer_for_queryset.data)
