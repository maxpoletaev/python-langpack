from copy import deepcopy


class safedict(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def safe_format(source, **kwargs):
    return source.format_map(safedict(**kwargs))


def deep_merge(result, *dicts):
    for source in dicts:
        for key, value in source.items():
            if key in result and isinstance(result[key], dict):
                deep_merge(result[key], value)
            else:
                result[key] = deepcopy(value)
    return result
