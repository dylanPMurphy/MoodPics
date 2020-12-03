from django.contrib import admin
from .models import * # add this
from login_reg.models import *


class UserAdmin(admin.ModelAdmin):  # add this
    list_display = ('username', 'email', 'password') # add this

admin.site.register(User, UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'mood', 'poster')
admin.site.register(Post, PostAdmin)