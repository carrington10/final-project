from django.contrib import admin
from animeweb.models import Friend, Comment,Post, Wallpost
# Register your models here.
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Comment)
admin.site.register(Wallpost)
