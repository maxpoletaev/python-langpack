from functools import partial
pluralizers = {}

ERR_INTEGER = 'Pluralizers support only integer values. Obtained {}.'


def register(fn=None, lang=None):
    if fn is None:
        return partial(register, lang=lang)
    if not lang:
        lang = fn.__name__
    pluralizers[lang] = fn
    return fn


@register
def en(count):
    if count == 0:
        return 'zero'
    if count == 1:
        return 'one'
    return 'many'


@register
def ru(count):
    if count == 0:
        return 'zero'
    if count % 100 in (11, 12, 13, 14):
        return 'many'
    if count % 10 == 1:
        return 'one'
    if count % 10 in (2, 3, 4):
        return 'two'
    else:
        return 'many'


def get_plural_form(lang, count):
    assert isinstance(count, int), ERR_INTEGER.format(type(count))
    return pluralizers[lang](count)
