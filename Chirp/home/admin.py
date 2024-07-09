from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(ChirpModel)
admin.site.register(LikeModel)
admin.site.register(CommentModel)
admin.site.register(ChatModel)