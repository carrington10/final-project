from django.contrib import admin
from .models import Friend, Comment,Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Comment)
