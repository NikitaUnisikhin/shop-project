from core.apps.orders.models import Order, OrderItem


def get_user_orders(user):
    return Order.objects.filter(buyer=user)


def get_order_items(order):
    return OrderItem.objects.filter(order=order)


def get_seller_order_items(seller):
    return OrderItem.objects.filter(seller=seller)
