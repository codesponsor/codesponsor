from django.contrib import admin
from django.db.models import Count, Q

from .models import Click, Impression


class GithubAgentImpressionsFilter(admin.SimpleListFilter):
    title = 'GitHub user agent'
    parameter_name = 'github_agent'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Yes'),
            ('0', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.annotate(
                Count('id')).filter(user_agent__contains='github-camo')
        elif self.value() == '0':
            return queryset.annotate(
                Count('id')).filter(~Q(user_agent__contains='github-camo'))

        return queryset


# Stubbed as example for future usage
def blacklist(modeladmin, requet, queryset):
    # queryset.update(
    #     blacklisted=True
    # )
    pass


blacklist.short_description = 'Mark selected as blacklisted'


class ClickAdmin(admin.ModelAdmin):
    actions = [blacklist]
    date_hierarchy = 'created_at'
    list_display = [
        'sponsor',
        'property',
        'sponsorship',
        'ip_address',
        'referer',
        'created_at',
    ]
    readonly_fields = [
        'sponsor',
        'property',
        'sponsorship',
        'ip_address',
        'user_agent',
        'is_bot',
        'referer',
        'created_at',
        'updated_at',
    ]
    ordering = [
        'created_at',
    ]
    list_filter = [
        'sponsor',
        'property',
        'created_at',
    ]
    search_fields = [
        'ip_address',
        'sponsor__name',
        'property__name',
        'sponsorship__token',
    ]


class ImpressionAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = [
        'sponsor',
        'property',
        'sponsorship',
        'ip_address',
        'created_at',
    ]
    readonly_fields = [
        'sponsor',
        'property',
        'sponsorship',
        'ip_address',
        'user_agent',
        'is_bot',
        'created_at',
        'updated_at',
    ]
    ordering = [
        'created_at',
    ]
    list_filter = [
        'sponsor',
        'property',
        'created_at',
        GithubAgentImpressionsFilter,
    ]
    search_fields = [
        'ip_address',
        'sponsor__name',
        'property__name',
        'sponsorship__token',
    ]


admin.site.register(Click, ClickAdmin)
admin.site.register(Impression, ImpressionAdmin)
