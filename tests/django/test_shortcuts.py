from langpack.contrib.django import trans, trans_lazy
from nose import tools as test

from .cases import AppTestCase


class TestShortcuts(AppTestCase):
    def setup(self):
        translator = self.get_translator()
        translator.add_translations('en', translations={'foo': 'bar'})

    def test_trans(self):
        test.assert_equal(trans('foo'), 'bar')
        test.assert_equal(trans_lazy('foo'), 'bar')
