# """eventhandler path Configuration
#
# The `pathpatterns` list routes paths to views. For more information please see:
#     https://docs.djangoproject.com/en/1.11/topics/http/paths/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a path to pathpatterns:  path(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a path to pathpatterns:  path(r'^$', Home.as_view(), name='home')
# Including another pathconf
#     1. Import the include() function: from django.conf.paths import path, include
#     2. Add a path to pathpatterns:  path(r'^blog/', include('blog.paths'))
# """
from django.urls import path
from django.contrib import admin
from eventapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('candidate', views.candidate, name='candidate'),
    path('elements', views.elements, name='elements'),
    path('createevent', views.createevent, name='elements'),
    path('login', views.login1, name='login'),
    path('technical', views.technical, name='technical'),
    path('nontech', views.nontech, name='nontech'),
    path('cultural', views.cultural, name='cultural'),
    path('about', views.about, name='about'),

    path('price', views.price, name='price'),

    path('schedule', views.schedule, name='schedule'),

    path('signup', views.signup1, name='signup'),

    path('single', views.single, name='single'),

    path('logout', views.logout1, name='logout'),

    path('venue', views.venue, name='venue')

]