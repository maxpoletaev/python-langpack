from langpack.translators import Translator
from nose import tools as test


class MockLoader:
    def load_file(self, file_path):
        return {}


class TestTranslator:
    def setup(self):
        self.translator = Translator()

        self.translator.translations['en'] = {
            'hello': 'Hello, {name}!',
            'i_have_apples': {
                'zero': 'I have no apples',
                'one': 'I have one apple',
                'many': 'I have {count} apples',
            }
        }

    def test_register_loader(self):
        loader = MockLoader()
        self.translator.register_loader(loader, ['txt'])
        test.assert_equal(self.translator.loaders.get('txt'), loader)

    def test_get_current_lang(self):
        test.assert_equal(self.translator.get_current_lang(), 'en')

    def test_get_translation(self):
        translation = self.translator.get_translation('hello')
        test.assert_equal(translation, 'Hello, {name}!')

    def test_translate(self):
        result = self.translator.translate('hello', name='John')
        test.assert_equal(result, 'Hello, John!')

        result = self.translator.translate('i_have_apples', count=0)
        test.assert_equal(result, 'I have no apples')

        result = self.translator.translate('i_have_apples', count=10)
        test.assert_equal(result, 'I have 10 apples')

        result = self.translator.translate('unknown_str_id')
        test.assert_equal(result, 'unknown_str_id')

    def test_add_translations(self):
        self.translator.add_translations('en', 'blog', {
            'comments': 'Comments',
            'post': 'Post',
        })

        translations = self.translator.translations['en']
        test.assert_equal(translations.get('blog.comments'), 'Comments')
        test.assert_equal(translations.get('blog.post'), 'Post')
