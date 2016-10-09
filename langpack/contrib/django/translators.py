from langpack.translators import BaseTranslator
from django.utils import translation


class DjangoTranslator(BaseTranslator):
    def get_lang(self):
        language = translation.get_language()
        return language.split('-')[0]

    def set_lang(self, lang):
        message = ('DjangoTranslator uses native Django translations switcher. '
                   'Use django.utils.translation.activate() instead.')
        raise NotImplementedError(message)
