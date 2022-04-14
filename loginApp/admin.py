from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from loginApp.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ('username', 'password', 'branch')
    list_filter = ['branch']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('branch',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
