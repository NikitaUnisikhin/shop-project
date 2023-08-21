from django.urls import path
from . import views

urlpatterns = [
    path('addorder/', views.add_order),
    path('my/', views.my_orders),
    path('clients/', views.clients_orders),
]
