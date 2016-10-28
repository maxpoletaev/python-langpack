from django.utils.functional import lazy
from django.apps import apps


def trans(*args, **kwargs):
    app_config = apps.get_app_config('langpack')
    return app_config.translator.translate(*args, **kwargs)


def localize(*args, **kwargs):
    app_config = apps.get_app_config('langpack')
    return app_config.translator.localize(*args, **kwargs)


trans_lazy = lazy(trans, str)
