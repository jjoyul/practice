from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime
from .forms import ContactForm
from django.core.mail import send_mail

def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse("Homepage")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current.html', {'current_date': now})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})