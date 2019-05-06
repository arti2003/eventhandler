from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRegister(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    age = models.IntegerField(max_length=3,null=True)
    phone = models.IntegerField(max_length=15, null=True)
    gender = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "user_registration"
        verbose_name = "User Registration"

class CreateEvent(models.Model):
    event_name = models.CharField(max_length=100, null=True)
    event_type = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    fees = models.IntegerField(max_length=100, null=True)
    time1 = models.TimeField(null=True)
    email = models.CharField(max_length=100, null=True)
    event_details = models.CharField(max_length=500, null=True)
    registered = models.CharField(max_length=500, null=True, default=False)

    def __unicode__(self):
        return self.event_name

    class Meta:
        db_table = "create_event"
        verbose_name = "Create Event"