from langpack.translators import Translator
from langpack import loaders, formatters
from datetime import datetime
import random
import os

BASE_DIR = os.path.dirname(__file__)


# Initialize translator, loader and formatter
translator = Translator()
translator.add_loader(loaders.YamlLoader(), ['yaml', 'yml'])
translator.add_formatter(formatters.format_datetime, ['datetime'])
translator.load_directory(os.path.join(BASE_DIR, 'locales'))


# Cretae shortcuts and init data
trans = translator.translate
localize = translator.localize
today = datetime.today()
message_count = random.randint(0, 10)


def print_info():
    print(trans('common.welcome', name='John'))
    print(trans('common.today', date=localize(today, 'full')))
    print(trans('common.new_messages', count=message_count))
    print()


# Activate English and print several strings
translator.set_lang('en')
print_info()

# Activate Russian and print several strings
translator.set_lang('ru')
print_info()
