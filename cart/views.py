from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem
from django.utils.crypto import get_random_string

def _get_cart(request):
    """Lấy hoặc tạo Cart dựa trên user hoặc session_id"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_id = request.session.get('cart_session_id')
        if not session_id:
            session_id = get_random_string(32)
            request.session['cart_session_id'] = session_id
        cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)

        cart = _get_cart(request)

        # Kiểm tra xem sản phẩm đã có trong giỏ chưa
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return redirect('cart:cart_detail')

    return redirect('product_list')


def cart_detail(request):
    cart = _get_cart(request)
    items = cart.items.select_related('product').all()
    total = sum(item.product.price * item.quantity for item in items)

    context = {
        'cart': cart,
        'items': items,
        'total': total,
    }
    return render(request, 'cart/cart_detail.html', context)


def update_cart_item(request, item_id):
    if request.method == 'POST':
        cart = _get_cart(request)
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()

    return redirect('cart:cart_detail')


def remove_cart_item(request, item_id):
    cart = _get_cart(request)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    return redirect('cart:cart_detail')

def checkout(request):
    # logic thanh toán
    return render(request, 'cart/checkout.html')
