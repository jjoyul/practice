from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse("Homepage")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current.html', {'current_date': now})