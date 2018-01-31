from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
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

            recipients = ['team@codesponsor.io']

            send_mail(subject, content, f"{name} <{email}>", recipients)
            messages.success(request, 'Success!')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
