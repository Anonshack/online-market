from django.core.exceptions import ObjectDoesNotExist
from .views import _cart_id
from .models import CartItem, Cart


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            
            cart = Cart.objects.get(session_id=_cart_id(request))            
            cart_items = CartItem.objects.filter(cart=cart)
            
            for cart_item in cart_items:
                cart_count += cart_item.quantity
            
        except ObjectDoesNotExist:
            cart_count = 0
            
    return dict(cart_count=cart_count)
