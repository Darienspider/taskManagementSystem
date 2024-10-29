from django.contrib import admin
from .models import *

# Register your models here.
# since i am using a custom user model for authentication

admin.site.register(Task)
admin.site.register(Assignment)
admin.site.register(Notification)
