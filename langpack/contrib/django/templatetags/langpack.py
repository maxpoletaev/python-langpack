from langpack.contrib.django import shortcuts
from django.template import Library

register = Library()


@register.simple_tag
def trans(str_id, *args, **kwargs):
    return shortcuts.trans(str_id, *args, **kwargs)
