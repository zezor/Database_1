from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import UserManager, User


# Register your models here.
# class UserAdmin(DefaultUserAdmin):
#     list_display = ('email','is_staff')
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','username', 'is_staff')