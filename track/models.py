from django.db import models
from app.models import Property, Sponsor, Sponsorship


class Click(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    sponsorship = models.ForeignKey(Sponsorship, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    is_bot = models.BooleanField(default=False)
    referer = models.TextField(null=True)

    def __str__(self):
        return self.ip_address


class Impression(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    sponsorship = models.ForeignKey(Sponsorship, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.ip_address