from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRegister(models.Model):
    id = models.AutoField(primary_key=True)
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
    id =models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100, null=True)
    event_type = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=50, null=True)
    date = models.DateField(null=True)
    fees = models.IntegerField(max_length=100, null=True)
    time1 = models.TimeField(null=True)
    email = models.CharField(max_length=100, null=True)
    event_details = models.CharField(max_length=500, null=True)
    registered = models.CharField(max_length=500, null=True, default="False")

    def __unicode__(self):
        return self.event_name

    class Meta:
        db_table = "create_event"
        verbose_name = "Create Event"

class Participate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=True)
    event = models.OneToOneField(CreateEvent, on_delete=True)

    def __unicode__(self):
        return self.user

    class Meta:
        db_table = "participate"
        verbose_name = "Participate"

class Registered1(models.Model):
    user_id = models.OneToOneField(User, on_delete=True)
    event_id = models.OneToOneField(Participate, on_delete=True)

    def __unicode__(self):
        return self.user_id

    class Meta:
        db_table = "registered"
        verbose_name = "Registered"


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "contact"
        verbose_name = "Contact"