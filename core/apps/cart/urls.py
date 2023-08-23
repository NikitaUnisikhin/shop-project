from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/', views.cart),
    path('api/cart/products/add/', views.add_product),
    path('api/cart/products/delete/', views.delete_cart_item)
]
