from __future__ import unicode_literals
from django.contrib import admin
from .models import UserRegister, CreateEvent


# Register your models here.
admin.site.register(UserRegister)
admin.site.register(CreateEvent)