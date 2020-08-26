from django.contrib import admin
from .models import User, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'like', 'date_created', 'user')

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
