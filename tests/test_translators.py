from langpack.translators import Translator, TranslationStore
from nose import tools as test
from datetime import datetime
from unittest import mock
import os


class TestTranslator:
    def setup(self):
        self.translator = Translator()

    def test_add_loader(self):
        loader = mock.Mock()
        self.translator.add_loader(loader, ['txt'])
        test.assert_equal(self.translator._loaders['txt'], loader)

    def test_get_lang(self):
        test.assert_equal(self.translator.get_lang(), 'en')

    def test_get_template(self):
        self.translator._translations['en'] = TranslationStore({
            'hello': 'Hello, {name}!',
        })
        translation = self.translator.get_template('hello')
        test.assert_equal(translation, 'Hello, {name}!')

    def test_translate(self):
        self.translator._translations['en'] = TranslationStore({
            'hello': 'Hello, {name}!',
        })
        result = self.translator.translate('hello', name='John')
        test.assert_equal(result, 'Hello, John!')

        result = self.translator.translate('hello')
        test.assert_equal(result, 'Hello, {name}!')

        result = self.translator.translate('unknown_str_id')
        test.assert_equal(result, 'unknown_str_id')

    def test_translate_plural(self):
        self.translator._translations['en'] = TranslationStore({
            'i_have_apples': {
                'zero': 'I have no apples',
                'one': 'I have one apple',
                'many': 'I have {count} apples',
            }
        })

        result = self.translator.translate('i_have_apples', count=0)
        test.assert_equal(result, 'I have no apples')

        result = self.translator.translate('i_have_apples', count=1)
        test.assert_equal(result, 'I have one apple')

        result = self.translator.translate('i_have_apples', count=10)
        test.assert_equal(result, 'I have 10 apples')

    def test_add_translations(self):
        self.translator.add_translations('en', {
            'blog': {
                'comments': 'Comments',
                'post': 'Post',
            },
        })

        translations = self.translator._translations['en']
        test.assert_equal(translations['blog']['comments'], 'Comments')
        test.assert_equal(translations['blog']['post'], 'Post')

    def test_load_directory(self):
        loader = mock.Mock()
        loader.load_file.return_value = {'en': {'mainpage': {'foo': 'bar'}}}

        locale_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.translator._loaders['txt'] = loader
        self.translator.load_directory(locale_dir)

        test.assert_true(loader.load_file.called)

    def test_localize(self):
        self.translator._translations['en'] = TranslationStore({
            'datetime': {
                'formats': {
                    'short': '%d.%M.%Y',
                },
            },
        })

        def format_datetime(value, format, translator):
            format = translator.get_template('datetime.formats.' + format, default=format)
            return value.strftime(format)

        self.translator.add_formatter(format_datetime, ['datetime'])
        now = datetime.now()

        assert self.translator.localize(now, 'short') == now.strftime('%d.%M.%Y')
        assert self.translator.localize(now, '%d.%M.%Y') == now.strftime('%d.%M.%Y')


class TestTranslationStore:
    def setup(self):
        self.store = TranslationStore()

    def test_get(self):
        self.store['en'] = {
            'hello': 'Hello',
            'inner': {'hello': 'Inner hello'}
        }
        assert self.store.get('en', 'hello') == 'Hello'
        assert self.store.get('en', 'inner.hello') == 'Inner hello'
