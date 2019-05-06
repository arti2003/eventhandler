# -*- coding: utf-8 -*-

from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import hashlib
from django.utils import timezone
from django.core.mail import send_mail
import hashlib, datetime, random
from django.contrib.auth import authenticate, login, logout
from django.core.mail import BadHeaderError, send_mail
import smtplib, ssl
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserRegister,CreateEvent

from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def elements(request):
    return render(request, 'elements.html')

def login1(request):
    if (request.method == 'POST'):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        print(user)
        print(user_name)
        print(password)

        if user is not None:
            login(request, user)
            return render(request, 'candidate.html', {'username':user_name})
    else:
        return render(request, 'loginnew.html')


def candidate(request):
    return render(request, 'candidate.html')

def price(request):
    return render(request, 'price.html')


def createevent(request):
    if (request.method == 'POST'):
        event_name = request.POST.get('event_name')
        event_type = request.POST.get('event_type')
        location = request.POST.get('location')
        date = request.POST.get('date')
        email = request.POST.get('email')
        fees = request.POST.get('fees')
        time1 = request.POST.get('time1')
        event_details = request.POST.get('event_details')
        print(email)
        print(event_name)

        data = CreateEvent(
            event_name= event_name,
            event_type=event_type,
            location=location,
            date=date,
            email=email,
            fees=fees,
            time1=time1,
            event_details=event_details
        )
        data.save()
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.ehlo()
        connection.starttls()
        connection.login('eventhandlerofficial@gmail.com', 'eventhandler@123')
        connection.sendmail('eventhandlerofficial@gmail.com', email, (
                "Subject: Event Created" + "\n\n" + "Thank You " + str(
            event_name) + " for registering in Event Handler"))


        return render(request, 'candidate.html')
    else:
        return render(request, 'createevent.html')



def schedule(request):
    return render(request, 'schedule.html')


def signup1(request):
    if(request.method == 'POST'):
        username = request.POST.get('user_name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        email= request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)

        data = UserRegister(
            user=user,
            age=age,
            phone=phone,
            gender=gender
        )
        data.save()
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.ehlo()
        connection.starttls()
        connection.login('eventhandlerofficial@gmail.com', 'eventhandler@123')
        connection.sendmail('eventhandlerofficial@gmail.com', email, (
                    "Subject: Registered Sucessfull" + "\n\n" + "Thank You " + str(
                username) + " for registering in Event Handler"))
        return render(request, 'loginnew.html')
    else:
        return render(request, 'signupnew.html')

def single(request):

    return render(request, 'single-blog.html')

def venue(request):
    return render(request, 'venue.html')

def technical(request):
    data = CreateEvent.objects.filter(event_type='technical')

    return render(request, 'technical.html', {'data':data})

def cultural(request):
    data = CreateEvent.objects.filter(event_type='cultural')

    return render(request, 'cultural.html', {'data':data})

def nontech(request):
    data = CreateEvent.objects.filter(event_type='nonTechnical')

    return render(request, 'nontech.html', {'data':data})

def logout1(request):
    logout(request)
    return redirect('/')


