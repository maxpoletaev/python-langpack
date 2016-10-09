from nose import tools as test
from .cases import TemplateTestCase


class TestLangPackLibrary(TemplateTestCase):
    library = 'langpack'

    def setup(self):
        self.translator = self.get_translator()

        self.translator.add_translations('en', {
            'hello': 'Hello, {name}!',
        })

    def test_trans(self):
        result = self.render('{% trans "hello" name="John" %}')
        test.assert_equal(result, 'Hello, John!')

    def test_plural_tag(self):
        result = self.render('{% plural 0 zero="no cats" one="cat" many="cats" %}')
        test.assert_equal(result, 'no cats')
        result = self.render('{% plural 1 zero="no cats" one="cat" many="cats" %}')
        test.assert_equal(result, 'cat')
        result = self.render('{% plural 10 zero="no cats" one="cat" many="cats" %}')
        test.assert_equal(result, 'cats')

    def test_plural_filter(self):
        result = self.render('{{ 0|plural:"zero: no cats, one: cat, many: cats" }}')
        test.assert_equal(result, 'no cats')
        result = self.render('{{ 1|plural:"zero: no cats, one: cat, many: cats" }}')
        test.assert_equal(result, 'cat')
        result = self.render('{{ 10|plural:"zero: no cats, one: cat, many: cats" }}')
        test.assert_equal(result, 'cats')
