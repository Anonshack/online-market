
from django.http import request
from django.shortcuts import render
from store.models import Product

def home(request):
    search=request.GET.get("search") or ""
    products = Product.objects.filter(is_available=True)
    if request.method=="GET" and search:
        products = products.filter(name__contains=search)
    context = {
        'products': products,
        "search":search
    }
    return render(request, 'home.html', context)
