from django.contrib import admin
from app.models import Sponsor, Property, Sponsorship


class SponsorshipAdmin(admin.ModelAdmin):
    exclude = ('token',)
    readonly_fields = ('token',)


# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Property)
admin.site.register(Sponsorship, SponsorshipAdmin)