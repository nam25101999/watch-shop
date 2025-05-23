from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} tin nhắn đã được đánh dấu là đã đọc.")
    mark_as_read.short_description = "Đánh dấu các tin nhắn được chọn là đã đọc"

admin.site.register(Message, MessageAdmin)
