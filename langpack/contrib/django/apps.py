from importlib import import_module
import os

from django.apps import apps, AppConfig

from .translator import DjangoTranslator
from . import settings


class LangPackConfig(AppConfig):
    label = 'langpack'

    def ready(self):
        self.translator = self.create_translator()
        self.load_project_translations()
        if settings.LANGPACK_USE_APP_DIRS:
            self.load_apps_translations()

    def create_translator():
        translator = DjangoTranslator()
        for loader_path, extensions in settings.LANGPACK_LOADERS:
            loader_class = import_module(loader_path)
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
