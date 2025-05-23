from django.contrib.auth import get_user_model
from .models import Message
from django.db.models import Q

def chat_data(request):
    User = get_user_model()
    shop_user = User.objects.filter(is_staff=True).first()  # giả sử admin/staff là shop_user
    messages = []
    if request.user.is_authenticated and shop_user:
        messages = Message.objects.filter(
            Q(sender=request.user, receiver=shop_user) | Q(sender=shop_user, receiver=request.user)
        ).order_by('timestamp')
    return {
        'messages': messages,
        'shop_user': shop_user,
    }
