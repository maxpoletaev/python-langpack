from nose import tools as test
from .cases import TemplateTestCase


class TestLangPackLibrary(TemplateTestCase):
    library = 'langpack'

    def setup(self):
        self.translator = self.get_translator()
        self.translator.add_translations('en', translations={
            'hello': 'Hello, {name}!',
        })

    def test_trans(self):
        result = self.render('{% trans "hello" name="John" %}')
        test.assert_equal(result, 'Hello, John!')
