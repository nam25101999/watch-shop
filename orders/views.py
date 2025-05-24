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
@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        return redirect('cart:cart_detail')

    total = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'orders/checkout.html', context)

@login_required
def order_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)

    total = sum(item.price * item.quantity for item in order_items)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        order.payment_method = payment_method
        order.save()
        # Chuyển đến trang xác nhận hoặc trang danh sách đơn hàng
        return redirect('orders:order_list')  # hoặc hiển thị thông báo

    return render(request, 'orders/order_payment.html', {
        'order': order,
        'order_items': order_items,
        'total': total,
    })
@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})