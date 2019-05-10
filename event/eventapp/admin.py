from __future__ import unicode_literals
from django.contrib import admin
from .models import UserRegister, CreateEvent, Participate, Registered1, Contact


# Register your models here.
admin.site.register(UserRegister)
admin.site.register(CreateEvent)
admin.site.register(Participate)
admin.site.register(Registered1)
admin.site.register(Contact)