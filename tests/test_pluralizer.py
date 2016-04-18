from langpack import pluralizers
from nose import tools as test


def test_register():
    @pluralizers.register
    def somelang1(count):
        pass

    @pluralizers.register()
    def somelang2(count):
        pass

    @pluralizers.register(lang='somelang3')
    def somelang4(count):
        pass

    saved_registry = pluralizers.pluralizers.copy()
    test.assert_equal(pluralizers.pluralizers['somelang1'], somelang1)
    test.assert_equal(pluralizers.pluralizers['somelang2'], somelang2)
    test.assert_equal(pluralizers.pluralizers['somelang3'], somelang4)
    pluralizers.pluralizers = saved_registry  # cleanup


def test_ru():
    test.assert_equal(pluralizers.ru(0), 'zero')
    test.assert_equal(pluralizers.ru(1), 'one')
    test.assert_equal(pluralizers.ru(2), 'two')
    test.assert_equal(pluralizers.ru(3), 'two')
    test.assert_equal(pluralizers.ru(5), 'many')
    test.assert_equal(pluralizers.ru(11), 'many')

    test.assert_equal(pluralizers.ru(1000), 'many')
    test.assert_equal(pluralizers.ru(1101), 'one')
    test.assert_equal(pluralizers.ru(1102), 'two')
    test.assert_equal(pluralizers.ru(1103), 'two')


def test_en():
    test.assert_equal(pluralizers.en(0), 'zero')
    test.assert_equal(pluralizers.en(1), 'one')
    test.assert_equal(pluralizers.en(2), 'many')


def test_get_plural_form():
    test.assert_equal(pluralizers.get_plural_form('en', 0), 'zero')
    with test.assert_raises(AssertionError):
        pluralizers.get_plural_form('en', 0.1)
