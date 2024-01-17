from django.shortcuts import render
from cart.views import _cart_id
# Create your views here.
from cart.models import *
from cart.views import *
from store.models import * 

def total(request):
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
        cart_items1 = CartItem.objects.all()
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        total = quantity = 0
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
        tax=(total * 2) / 100
        gen_total = total - tax
  
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax':tax,
        'gen_total':gen_total,
        'cart_items1':cart_items1
    }
    return render(request, 'total.html', context)