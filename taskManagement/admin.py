from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.
# since i am using a custom user model for authentication
class UserAdmin(BaseUserAdmin):
    model = User


admin.site.register(Task)
admin.site.register(User)
