def safe_format(source, **kwargs):
    # TODO: perfomance problem
    while True:
        try:
            return source.format(**kwargs)
        except KeyError as e:
            e = e.args[0]
            kwargs[e] = '{%s}' % e
