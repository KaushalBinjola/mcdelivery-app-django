from django.contrib import admin
from .models import my_user
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserAdminConfig(UserAdmin):
    search_fields = ("email", "username")
    list_filter = ("is_active", "is_staff")
    list_display = ("email", "username", "is_active", "is_staff")

    fieldsets = (
        ("Details", {"fields": ("username", "address", "email", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )
    add_fieldsets = (
        ("Details", {"fields": ("username", "address", "email", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )


admin.site.register(my_user, UserAdminConfig)
