from langpack.translators import Translator
from langpack.loaders import YamlLoader
import random
import os

BASE_DIR = os.path.dirname(__file__)


# Initialize translator
translator = Translator()
translator.register_loader(YamlLoader(), ['yaml', 'yml'])
translator.load_directory(os.path.join(BASE_DIR, 'locale'))


# Cretae shortcut for translation function
trans = translator.translate


# Just use!

translator.switch_lang('en')
print('-- en ---')
print(trans('mainpage.welcome', name='John'))
print(trans('mainpage.new_messages', count=random.randint(0, 10)))
print('')

translator.switch_lang('ru')
print('-- ru ---')
print(trans('mainpage.welcome', name='John'))
print(trans('mainpage.new_messages', count=random.randint(0, 10)))
