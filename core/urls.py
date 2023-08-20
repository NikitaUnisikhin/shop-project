from django.contrib import admin
from django.urls import path
from core.apps.catalog import views as view_catalog
from core.apps.basket import views as view_basket
from core.apps.account import views as view_account
from django.contrib.auth import views as views_auth
from core.apps.orders import views as view_orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/add', view_catalog.creating_product),
    path('catalog/<int:product_id>', view_catalog.product),
    path('basket/<int:product_id>/add', view_basket.add_product),
    path('basket/<int:item_id>', view_basket.basket_item_delete),
    path('basket/', view_basket.index),
    path('account/register', view_account.register),
    path('account/login/', views_auth.LoginView.as_view(template_name='login.html')),
    path('account/profile', view_account.profile),
    path('orders/add', view_orders.add),
    path('orders/my', view_orders.my_orders),
    path('orders/clients', view_orders.clients_orders),
    path('', view_catalog.index)
]
