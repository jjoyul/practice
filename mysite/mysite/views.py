from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
import datetime

def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse("Homepage")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)