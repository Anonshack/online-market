from django.db.models import Q

from cart.views import _cart_id
from django.shortcuts import get_object_or_404, render, redirect
from main.models import Category
from .models import Product
from cart.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from store.models import Product
from .forms import *
# def home(request):
#     search=request.GET.get("search") or ""
#     products = Product.objects.filter(is_available=True)
#     if request.method=="GET" and search:
#         products = products.filter(name__contains=search)
#     context = {
#         'products': products,
#         "search":search
#     }
#     return render(request, 'home.html', context)

from comment.forms import *
from comment.models import Comment


def store(request, category_slug=None):
    if category_slug == None:
        products = Product.objects.filter(is_available=True).order_by('id')
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categories).order_by('id')

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    search=request.GET.get("search") or ""
    products = Product.objects.filter(is_available=True)
    if request.method == "GET" and search:
          products = products.filter(name__contains=search)
    context = {
        'products': paged_products,
        'product_count': products.count(),
        'search' :search,
    }
    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug)
    cart_in = CartItem.objects.filter(cart__session_id=_cart_id(request), product=product).exists()
    context = {
        'product': product,
        'cart_in': cart_in
    }
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
    context["comments"] = Comment.objects.filter(product=product)
    return render(request, 'product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
    if keyword:
        products = Product.objects.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword))
    
    context = {
        'products': products,
        'product_count': products.count()
    }
    return render(request, 'store.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store') 
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store')  
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})
