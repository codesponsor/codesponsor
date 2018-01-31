from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
import requests


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

            results = requests.post(
                "https://api.mailgun.net/v3/{0}/messages".format(
                    settings.MAILGUN_SENDING_DOMAIN),
                auth=("api", settings.MAILGUN_API_KEY),
                data={
                    "from": from_email,
                    "to": recipients,
                    "subject": subject,
                    "text": content
                })

            messages.success(request, 'Success!')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
