from langpack.contrib.django import shortcuts
from django.template import Library

register = Library()


@register.simple_tag
def trans(*args, **kwargs):
    return shortcuts.trans(*args, **kwargs)


@register.simple_tag
def localize(*args, **kwargs):
    return shortcuts.localize(*args, **kwargs)
