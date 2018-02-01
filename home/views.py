from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

import requests

from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


def mail(request):
    '''Send email via mailgun'''
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            from_email = name + "<" + email + ">"
            recipients = ['team@codesponsor.io']

            send_mail(subject, content, from_email, recipients)

            messages.success(request, 'Success!')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
