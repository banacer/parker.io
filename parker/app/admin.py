from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import User,Device

admin.site.register(User)
admin.site.register(Device)