from django.db import models
from django.template.defaultfilters import slugify
from netfields import InetAddressField, NetManager


class Sponsor(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sponsor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField()

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name


class Sponsorship(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    redirect_url = models.URLField()

    def __str__(self):
        return self.sponsor.name + " -> " + self.property.name


class Click(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    sponsorship = models.ForeignKey(Sponsorship, on_delete=models.CASCADE)
    ip_address = InetAddressField()
    user_agent = models.TextField()
    is_bot = models.BooleanField(default=False)
    referer = models.TextField()
    objects = NetManager()

    def __str__(self):
        return self.ip_address


class Impression(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    sponsorship = models.ForeignKey(Sponsorship, on_delete=models.CASCADE)
    ip_address = InetAddressField()
    user_agent = models.TextField()
    is_bot = models.BooleanField(default=False)
    objects = NetManager()

    def __str__(self):
        return self.ip_address