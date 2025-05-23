from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product
from django.contrib import messages

@login_required
def wishlist_view(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    products = wishlist.products.all()
    return render(request, 'wishlist/wishlist.html', {'products': products})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if product in wishlist.products.all():
        messages.info(request, "Sản phẩm đã có trong wishlist.")
    else:
        wishlist.products.add(product)
        messages.success(request, "Đã thêm sản phẩm vào wishlist.")
    return redirect('wishlist:wishlist')

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, "Đã xoá sản phẩm khỏi wishlist.")
    else:
        messages.info(request, "Sản phẩm không tồn tại trong wishlist.")
    return redirect('wishlist:wishlist')

