import sys
this_module = sys.modules[__name__]


def en(count):
    if count == 0:
        return 'zero'
    if count == 1:
        return 'one'
    return 'many'


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


def get_plural_form(count, lang):
    return getattr(this_module, lang)(count)
