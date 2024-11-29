"""
URL configuration for rambhakthanumanji project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),        # Home page


    path('about/', views.about, name='about'),      # about page

    path('tt/', views.tt, name='tt'),      # tt page

    path('practise/', views.practise, name='practise'),      # practise page

    path('out/', views.out, name='out'),      # out page

    path('off/', views.off, name='off'),      # off page

    path('menu/', views.menu, name='menu'),      # menu page

    path('contact/', views.contact, name='contact'),      # contact page

    path('booking/', views.booking, name='booking'),      # booking page

    path('blog/', views.blog, name='blog'),      # blog page

  

]
