# views.py trong app orders
from django.shortcuts import redirect
from .models import Order, OrderItem
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from cart.models import Cart, CartItem
from .forms import ShippingAddressForm
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def create_order(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return redirect('cart:cart_detail')

    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        return redirect('cart:cart_detail')

    order = Order.objects.create(
        user=request.user,
        created_at=timezone.now(),
        total=0,  # sẽ cập nhật sau
        payment_method="COD",  # hoặc request.POST.get('payment_method')
        shipping_address="Chưa cập nhật"  # hoặc request.POST.get('shipping_address')
    )

    total_price = 0
    for item in cart_items:
        item_total = item.product.price * item.quantity
        total_price += item_total

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    order.total = total_price
    order.save()

    cart_items.delete()  # Xoá giỏ hàng
    cart.delete()  # hoặc giữ lại nếu cần

    return redirect('orders:order_list')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})
@login_required
def edit_shipping_address(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = ShippingAddressForm(instance=order)

    return render(request, 'orders/edit_shipping_address.html', {'form': form, 'order': order})
def checkout(request):
    # logic thanh toán
    return render(request, 'orders/checkout.html')
@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})