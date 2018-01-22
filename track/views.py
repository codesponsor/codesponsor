from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from app.models import Sponsorship
from .models import Click, Impression


def pixel(request, token):
    try:
        sponsorship = Sponsorship.objects.get(token=token)
    except Sponsorship.DoesNotExist:
        sponsorship = None

    user_agent = request.META.get('HTTP_USER_AGENT', None)
    referer = request.META.get('HTTP_REFERER', 'None')
    ip_address = get_client_ip(request)

    if sponsorship:
        if ip_address:
            print("IP ADDRESS: {0}".format(ip_address))

            impression = Impression(sponsorship=sponsorship)

            # Denormalize for speed of query
            impression.property_id = sponsorship.property_id
            impression.sponsor_id = sponsorship.sponsor_id
            impression.user_agent = user_agent
            impression.ip_address = ip_address

            impression.is_bot = False  # TODO

            impression.save()

    BASE_DIR = getattr(settings, "BASE_DIR", None)
    image_data = open(BASE_DIR + "/static/images/pixel.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")


def track_click(request, token):
    try:
        sponsorship = Sponsorship.objects.get(token=token)
    except Sponsorship.DoesNotExist:
        sponsorship = None

    user_agent = request.META.get('HTTP_USER_AGENT', None)
    referer = request.META.get('HTTP_REFERER', 'None')
    ip_address = get_client_ip(request)

    if sponsorship:
        if ip_address:
            print("IP ADDRESS: {0}".format(ip_address))

            click = Click(sponsorship=sponsorship)

            # Denormalize for speed of query
            click.property_id = sponsorship.property_id
            click.sponsor_id = sponsorship.sponsor_id
            click.user_agent = user_agent
            click.referer = referer
            click.ip_address = ip_address

            click.is_bot = False  # TODO

            click.save()

            return HttpResponseRedirect(sponsorship.redirect_url)

        else:
            print("IP Address is not provided in request")
            return HttpResponseRedirect('https://codesponsor.io')

    else:
        print("Sponsorship not found for token: {0}".format(token))
        return HttpResponseRedirect('https://codesponsor.io')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip