"""
URL configuration for UrbanDjango project.

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
from task1.views import info
from task2.views import index, index2
from task3.views import platform_, games_, cart_
from task4.views import get_menu, games, cart
from task5.views import sign_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', info),
    path('func/', index),
    path('class/', index2.as_view()),
    path('platform_/', platform_),
    path('games_/', games_),
    path('cart_/', cart_),
    path('games/', games),
    path('cart/', cart),
    path('menu/', get_menu),
    path('django/', sign_by_django),
    path('html/', sign_up_by_html),
]
