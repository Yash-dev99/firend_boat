from .models import *
from django.contrib import admin

# Register your models here.

admin.site.register(UserDim)
admin.site.register(UserDetail)
admin.site.register(CommentDim)
admin.site.register(ConversationDim)
admin.site.register(ConversationUser)
admin.site.register(LoginLog)
admin.site.register(MessagesDim)
admin.site.register(PostDim)
admin.site.register(PostVote)
admin.site.register(SubboatDim)
admin.site.register(SubboatJoin)
admin.site.register(UserPassword)
