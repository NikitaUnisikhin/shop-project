from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addproduct/', views.add_product),
    path('<int:item_id>/', views.delete_cart_item)
]
