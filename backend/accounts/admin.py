from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class SehatUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Sehat Setu", {"fields": ("role", "phone_number", "city")}),
    )
    list_display = ("username", "email", "role", "is_staff")
