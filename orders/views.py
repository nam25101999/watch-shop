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

def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()
    total = order.total

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', 'cod')
        order.payment_method = payment_method
        order.payment_status = 'unpaid'  # Mặc định chưa thanh toán, có thể thay đổi logic nếu muốn
        order.save()

        messages.success(request, 'Phương thức thanh toán đã được cập nhật. Vui lòng thực hiện thanh toán theo hướng dẫn.')

        # Có thể redirect đến trang xác nhận hoặc trang thông tin thanh toán
        return redirect('payment_confirmation', order_id=order.id)

    # Lấy param để highlight button nếu load lại trang có method query param
    method = request.GET.get('method', 'cod')

    return render(request, 'payment.html', {
        'order': order,
        'order_items': order_items,
        'total': total,
        'selected_method': method,
    })


def payment_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/payment_confirmation.html', {
        'order': order,
    })

@login_required
def payment_view(request, order_id):
    # Lấy đơn hàng theo order_id và user hiện tại
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Lấy các món hàng thuộc đơn hàng
    order_items = OrderItem.objects.filter(order=order)
    
    # Tổng tiền được lưu trong order.total
    total = order.total
    
    if request.method == 'POST':
        # Lấy phương thức thanh toán từ form gửi lên
        payment_method = request.POST.get('payment_method', 'cod')
        order.payment_method = payment_method
        order.payment_status = 'unpaid'  # Mặc định trạng thái chưa thanh toán
        order.save()
        
        messages.success(request, 'Phương thức thanh toán đã được cập nhật. Vui lòng thực hiện thanh toán theo hướng dẫn.')
        
        # Chuyển hướng đến trang xác nhận thanh toán (có thể tuỳ chỉnh)
        return redirect('payment_confirmation', order_id=order.id)
    
    # Nếu GET request, hiển thị trang thanh toán với dữ liệu cần thiết
    return render(request, 'orders/payment.html', {
        'order': order,
        'order_items': order_items,
        'total': total,
    })
from django.shortcuts import render, get_object_or_404

def payment_bank(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    # Lấy tổng tiền từ order
    total = order.total

    if request.method == "POST":
        # Xử lý xác nhận thanh toán chuyển khoản
        # VD: lưu trạng thái đơn hàng, gửi mail, ...
        pass

    return render(request, 'orders/payment_bank.html', {
        'order': order,
        'total': total,
    })

def payment_cod(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # logic xử lý thanh toán COD
    return render(request, 'orders/payment_cod.html', {'order': order})
def payment_momo(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # logic xử lý thanh toán ví MoMo
    return render(request, 'orders/payment_momo.html', {'order': order})
