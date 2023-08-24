from django.urls import path
from . import views

urlpatterns = [
    path('orders/add/', views.add_order),
    path('orders/my/', views.my_orders),
    path('orders/clients/', views.clients_orders),
]
