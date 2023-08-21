from core.apps.cart.models import CartItem, Cart


def get_user_cart(user):
    return Cart.objects.get_or_create(buyer=user)[0]


def get_user_cart_items(user):
    return CartItem.objects.filter(cart=get_user_cart(user))
