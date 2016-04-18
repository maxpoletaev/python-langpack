import os

from django.apps import apps, AppConfig
from langpack.utils import import_class
from langpack import pluralizers

from langpack.contrib.django.translators import DjangoTranslator
from langpack.contrib.django import settings


class LangPackConfig(AppConfig):
    name = 'langpack.contrib.django'
    label = 'langpack'

    def ready(self):
        self.translator = self.create_translator()
        self.register_pluralizers()
        self.load_project_translations()
        if settings.LANGPACK_USE_APP_DIRS:
            self.load_apps_translations()

    def register_pluralizers(self):
        for lang, fn_path in settings.LANGPACK_PLURALIZERS.items():
            pluralizer = import_class(fn_path)
            pluralizers.register(pluralizer, lang)

    def create_translator(self):
        translator = DjangoTranslator()
        for loader_path, extensions in settings.LANGPACK_LOADERS:
            loader_class = import_class(loader_path)
            translator.register_loader(loader_class(), extensions)
            return translator

    def load_project_translations(self):
        for locale_dir in settings.LANGPACK_DIRS:
            if os.path.isdir(locale_dir):
                self.translator.load_directory(locale_dir)

    def load_apps_translations(self):
        for app_label, app_config in apps.app_configs.items():
            locale_dir = os.path.join(app_config.path, settings.LANGPACK_APP_DIR_NAME)
            if os.path.isdir(locale_dir):
                self.translator.load_directory(locale_dir)
