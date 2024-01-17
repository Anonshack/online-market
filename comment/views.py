from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from store.models import Product
from .forms import CommentForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_detail', product_id=product.id)
        else:
            print(form.errors)
    else:
        form = CommentForm()
    return render(request, 'product_detail.html', {'product': product, 'comments': comments, 'form': form})
