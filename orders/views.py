from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_list(request):
    # Lấy danh sách đơn hàng của user đang đăng nhập, sắp xếp theo ngày tạo mới nhất
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    # Lấy chi tiết đơn hàng của user đang đăng nhập (bảo mật)
    order = get_object_or_404(Order, id=order_id, user=request.user)
    # Lấy các món hàng trong đơn (OrderItem)
    items = order.items.all()
    return render(request, 'orders/order_detail.html', {'order': order, 'items': items})
