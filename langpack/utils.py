from importlib import import_module


class safedict(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def safe_format(source, **kwargs):
    return source.format_map(safedict(**kwargs))


def import_class(path):
    _p = path.split('.')
    package, class_name = '.'.join(_p[:-1]), _p[-1:][0]
    return getattr(import_module(package), class_name)
