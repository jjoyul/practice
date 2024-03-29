"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .views import hello, my_homepage_view, current_datetime, contact
from books.views import search, search_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', my_homepage_view),
    path('time/', current_datetime),
    path('search-form/', search_form),
    path('search/', search),
    path('contact/', contact),
]
