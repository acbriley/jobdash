from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Job, User
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    ordering = ("email",)
    list_display = ["email"]


admin.site.register(Job)
admin.site.register(User, UserAdmin)
