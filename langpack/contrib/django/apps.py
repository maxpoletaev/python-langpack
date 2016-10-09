import os

from django.utils.module_loading import import_string
from django.apps import apps, AppConfig
from langpack import pluralizers

from langpack.contrib.django.translators import DjangoTranslator
from langpack.contrib.django import settings


class LangPackConfig(AppConfig):
    name = 'langpack.contrib.django'
    label = 'langpack'

    def ready(self):
        self.translator = self.create_translator()
        self.register_pluralizers()
        self.register_formatters()
        self.load_project_translations()
        if settings.LANGPACK_USE_APP_DIRS:
            self.load_apps_translations()

    def register_pluralizers(self):
        for lang, fn_path in settings.LANGPACK_PLURALIZERS.items():
            pluralizer = import_string(fn_path)
            pluralizers.register(pluralizer, lang)

    def register_formatters(self):
        for formatter_path, types in settings.LANGPACK_FORMATTERS:
            formatter = import_string(formatter_path)
            self.translator.add_formatter(formatter, types)

    def create_translator(self):
        translator = DjangoTranslator()
        for loader_path, extensions in settings.LANGPACK_LOADERS:
            loader_class = import_string(loader_path)
            translator.add_loader(loader_class(), extensions)
            return translator

    def load_project_translations(self):
        for locale_dir in settings.LANGPACK_DIRS:
            if os.path.isdir(locale_dir):
                self.translator.load_directory(locale_dir, recursive=True)

    def load_apps_translations(self):
        for app_label, app_config in apps.app_configs.items():
            for dirname in settings.LANGPACK_APP_DIRS:
                locale_dir = os.path.join(app_config.path, dirname)
                if os.path.isdir(locale_dir):
                    self.translator.load_directory(locale_dir)
