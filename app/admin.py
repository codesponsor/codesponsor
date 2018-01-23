from django.contrib import admin

from app.models import Property, Sponsor, Sponsorship


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    ordering = ['name']
    list_filter = ['name', 'slug']
    search_fields = ['name', 'slug']


class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    ordering = ['name']
    list_filter = ['name', 'url']
    search_fields = ['name', 'url']


class SponsorshipAdmin(admin.ModelAdmin):
    exclude = ['token']
    readonly_fields = ('token', )
    list_display = ['redirect_url', 'token']
    ordering = ['redirect_url']
    list_filter = [
        'sponsor__name', 'sponsor__slug', 'property__name', 'property__url',
        'token'
    ]
    search_fields = [
        'sponsor__name', 'sponsor__slug', 'property__name', 'property__url',
        'token'
    ]


# Register your models here.
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Sponsorship, SponsorshipAdmin)
