from collections import defaultdict
import os

from .exceptions import TranslatorException
from .pluralizers import get_plural_form
from .utils import safe_format


class BaseTranslator:
    def __init__(self):
        self.translations = defaultdict(dict)
        self.loaders = {}

    def switch_lang(self):
        raise NotImplementedError()

    def get_current_lang(self):
        raise NotImplementedError()

    def register_loader(self, loader, extensions):
        for ext in extensions:
            self.loaders[ext] = loader

    def get_translation(self, str_id):
        lang = self.get_current_lang()
        return self.translations[lang].get(str_id)

    def translate(self, str_id, count=0, **kwargs):
        template = self.get_translation(str_id)
        lang = self.get_current_lang()
        if not template:
            return str_id
        if isinstance(template, dict):
            plural_index = get_plural_form(count, lang)
            template = template.get(plural_index)
        kwargs['count'] = count
        return safe_format(template, **kwargs)

    def load_directory(self, directory):
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            self.load_file(file_path)

    def load_file(self, file_path):
        *namespace, locale, ext = os.path.basename(file_path).split('_')
        namespace = '.'.join(namespace) if namespace else None

        try:
            loader = self.loaders[ext]
        except KeyError:
            raise TranslatorException(
                'No loader found for .{} file'.format(ext))

        translations = loader.load_file(file_path)
        self.add_translations(locale, namespace, translations)

    def add_translations(self, locale=None, namespace=None, translations={}):
        for str_id, value in translations.items():
            if namespace:
                str_id = '{}.{}'.format(namespace, str_id)
            self.translations[locale][str_id] = value


class Translator(BaseTranslator):
    def __init__(self, initial_lang='en', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_lang = initial_lang

    def get_current_lang(self):
        return self.current_lang

    def set_current_lang(self, lang):
        self.current_lang = lang
