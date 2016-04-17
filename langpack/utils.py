from importlib import import_module


def safe_format(source, **kwargs):
    # TODO: perfomance problem
    while True:
        try:
            return source.format(**kwargs)
        except KeyError as e:
            e = e.args[0]
            kwargs[e] = '{%s}' % e


def import_class(path):
    _p = path.split('.')
    package, class_name = '.'.join(_p[:-1]), _p[-1:][0]
    return getattr(import_module(package), class_name)
