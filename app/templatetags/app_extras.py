import re

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='search')
def search(value, search):
    return re.sub(search, 'SUBSTRING_THAT_NEVER_OCCURS', value)


@register.filter(name='replace')
def replace(value, replace):
    return re.sub('SUBSTRING_THAT_NEVER_OCCURS', replace, value)
