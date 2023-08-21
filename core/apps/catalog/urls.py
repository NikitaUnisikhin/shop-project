from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addproduct/', views.create_product),
]
