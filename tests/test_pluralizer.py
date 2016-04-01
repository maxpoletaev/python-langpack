from langpack import pluralizers
from nose import tools as test


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
