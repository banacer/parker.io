from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Device
from django.contrib.auth.models import User

admin.site.register(Device)