from django.contrib import admin
from .models import *
# Register your models here.

class UserAccountView(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'majina', 'password']

admin.site.register(UserAccount, UserAccountView)