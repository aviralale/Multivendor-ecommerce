from django.contrib import admin
from .models import ConversationMessage, Conversation
# Register your models here.
admin.site.register(Conversation)
admin.site.register(ConversationMessage)