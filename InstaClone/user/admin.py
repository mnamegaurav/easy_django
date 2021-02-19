from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from authentication.forms import UserForm, CustomUserChangeForm
# Register your models here.

User = get_user_model()

# ModelAdmin

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('bio', 'website')}),
        )
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('bio', 'website')}),
        )


admin.site.register(User, CustomUserAdmin)