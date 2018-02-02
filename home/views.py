import json

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token

import requests

from .forms import ContactForm


@ensure_csrf_cookie
def index(request):
    if request.method == 'GET':
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


@requires_csrf_token
def mail(request):
    '''Send email via mailgun'''
    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode('utf-8'))
        form = ContactForm(received_json_data)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            from_email = name + "<" + email + ">"
            recipients = ['team@codesponsor.io']

            send_mail(subject, content, from_email, recipients)

            status = 201

        else:
            status = 400

        return JsonResponse(data={'errors': form.errors}, status=status)

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
