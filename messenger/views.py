from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message
from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


User = get_user_model()

@login_required
def chat_view(request):
    shop_user = User.objects.filter(is_staff=True).first()  # Giả sử shop là tài khoản admin
    messages = Message.objects.filter(sender=request.user, receiver=shop_user) | \
               Message.objects.filter(sender=shop_user, receiver=request.user)
    return render(request, 'messenger/chat.html', {
        'messages': messages,
        'shop_user': shop_user
    })

@csrf_exempt
@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        receiver_id = request.POST.get('receiver_id')
        if content and receiver_id:
            try:
                receiver = User.objects.get(pk=receiver_id)
                Message.objects.create(sender=request.user, receiver=receiver, content=content)
                return JsonResponse({'status': 'ok'})
            except User.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Receiver not found'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing content or receiver_id'})
    return JsonResponse({'status': 'error', 'message': 'Invalid method'})


@staff_member_required
def admin_chat(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    admin_user = request.user

    # Lấy tất cả tin nhắn 2 chiều giữa user và admin
    messages = Message.objects.filter(
        Q(sender=user, receiver=admin_user) | Q(sender=admin_user, receiver=user)
    ).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=admin_user, receiver=user, content=content)
            return redirect('admin_chat', user_id=user.id)

    context = {
        'chat_user': user,
        'messages': messages,
    }
    return render(request, 'messenger/admin_chat.html', context)

@staff_member_required
def admin_chat_list(request):
    admin = request.user
    
    # Lấy tất cả user đã gửi tin nhắn đến admin
    users_sent_messages = User.objects.filter(
        sent_messages__receiver=admin
    ).distinct()

    # Hoặc, để lấy tất cả user có tin nhắn 2 chiều với admin:
    # users_with_messages = User.objects.filter(
    #     Q(sent_messages__receiver=admin) | Q(received_messages__sender=admin)
    # ).distinct()

    context = {
        'users': users_sent_messages,
    }
    return render(request, 'messenger/admin_chat_list.html', context)