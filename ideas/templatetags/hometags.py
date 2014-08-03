from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def replacespaces(value):
    return value.replace(' ', '_')

@register.filter
def filter_status(queryset, status):
    print(len(queryset.filter(status=status)))
    return queryset.filter(status=status)

@register.filter
def is_empty(queryset, status):
    if len(queryset.filter(status=status)) == 0:
        return True
    else:
        return False
