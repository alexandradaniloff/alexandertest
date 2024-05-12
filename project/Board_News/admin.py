from django.contrib import admin
from .models import User
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)