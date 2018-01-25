from app.models import Sponsorship
from celery import task

from .models import Impression


@task
def record_impression(token, user_agent, ip_address):
    sponsorship = Sponsorship.objects.get(token=token)
    impression = Impression(sponsorship=sponsorship)

    impression.property_id = sponsorship.property_id
    impression.sponsor_id = sponsorship.sponsor_id
    impression.user_agent = user_agent
    impression.ip_address = ip_address
    impression.is_bot = False  # TODO

    impression.save()
