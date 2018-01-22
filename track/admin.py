from django.contrib import admin
from .models import Click, Impression


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


admin.site.register(Click, ClickAdmin)
admin.site.register(Impression, ImpressionAdmin)