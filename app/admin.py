from django.contrib import admin
from app.models import Sponsor, Property, Sponsorship, Click, Impression


class ClickAdmin(admin.ModelAdmin):
    readonly_fields = (
        'sponsor',
        'property',
        'sponsorship',
        'ip_address',
        'user_agent',
        'is_bot',
        'referer',
    )


class ImpressionAdmin(admin.ModelAdmin):
    readonly_fields = (
        'sponsor',
        'property',
        'sponsorship',
        'ip_address',
        'user_agent',
        'is_bot',
    )


# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Property)
admin.site.register(Sponsorship)
admin.site.register(Click, ClickAdmin)
admin.site.register(Impression, ImpressionAdmin)