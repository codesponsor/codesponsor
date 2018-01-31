from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

import rollbar
from app.models import Sponsorship

from .tasks import record_click, record_impression


def pixel(request, token):
    try:
        sponsorship = Sponsorship.objects.get(token=token)
    except Sponsorship.DoesNotExist:
        sponsorship = None

    user_agent = request.META.get('HTTP_USER_AGENT', None)
    ip_address = get_client_ip(request)

    if sponsorship:
        if ip_address:
            record_impression.delay(token, user_agent, ip_address)

        else:
            rollbar.report_message(
                "[pixel] Pixel request without IP address for token: {0}".
                format(token), "warning")

    else:
        rollbar.report_message(
            "[pixel] Pixel request without sponsorship for token: {0}".format(
                token), "warning")

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
            record_click.delay(token, user_agent, ip_address, referer)

            return HttpResponseRedirect(sponsorship.redirect_url)

        else:
            rollbar.report_message(
                "[track_click] IP Address is not provided in request for token: {0}".
                format(token), "warning")
            return HttpResponseRedirect('https://codesponsor.io')

    else:
        rollbar.report_message(
            "[track_click] Sponsorship not found for token: {0}".format(token),
            "warning")
        return HttpResponseRedirect('https://codesponsor.io')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
