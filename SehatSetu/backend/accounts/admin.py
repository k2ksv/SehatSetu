from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'phone_number', 'age', 'gender', 'address', 'city')
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'date_created')
    list_filter = ('user_type', 'date_created')

admin.site.register(User, UserAdmin)
