from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart),
    path('cart/products/add/', views.add_product),
    path('cart/products/delete/', views.delete_cart_item)
]
