from langpack.contrib.django import shortcuts
from django.template import Library

register = Library()


@register.simple_tag
def trans(*args, **kwargs):
    return shortcuts.trans(*args, **kwargs)


@register.simple_tag
def localize(*args, **kwargs):
    return shortcuts.localize(*args, **kwargs)


@register.simple_tag(name='plural')
def plural_tag(*args, **kwargs):
    return shortcuts.plural(*args, **kwargs)


@register.filter(name='plural')
def plural_filter(value, arg):
    variants = {}
    for part in arg.split(','):
        k, v = part.split(':')
        variants[k.strip()] = v.strip()

    return shortcuts.plural(value, **variants)
