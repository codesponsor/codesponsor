from secrets import token_hex

from django.db import models
from django.template.defaultfilters import slugify


class Sponsor(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sponsor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name


class Sponsorship(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    redirect_url = models.URLField()
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = token_hex(16)
        super(Sponsorship, self).save(*args, **kwargs)

    def __str__(self):
        return self.sponsor.name + " -> " + self.property.name
