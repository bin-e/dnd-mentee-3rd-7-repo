from django.contrib import admin
from .models import User, Post, Comment, Hashtag, Like, History


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email', 'is_staff', 'is_superuser',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_created', 'user',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'content',)


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'number',)
    

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'query')

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(History, HistoryAdmin)
