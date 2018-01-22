from django.db import models
from django.template.defaultfilters import slugify

class Sponsor(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sponsor, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
