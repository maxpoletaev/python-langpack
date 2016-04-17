from django.template import Template, Context
from collections import defaultdict
from django.apps import apps


class AppTestCase:
    def get_translator(self):
        app = apps.get_app_config('langpack')
        app.translator.translations = defaultdict(dict)
        return app.translator


class TemplateTestCase(AppTestCase):
    library = None

    def render(self, content, **context_vars):
        load_tpl = ''
        if self.library:
            load_tpl = '{% load ' + self.library + ' %}'

        tpl = Template(load_tpl + content)
        context = Context(context_vars)
        return tpl.render(context)
