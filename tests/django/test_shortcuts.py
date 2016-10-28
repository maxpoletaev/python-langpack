from langpack.contrib.django import trans, localize, trans_lazy
from nose import tools as test
from datetime import datetime

from .cases import AppTestCase


class TestShortcuts(AppTestCase):
    def test_trans(self):
        translator = self.get_translator()
        translator.add_translations('en', {'foo': 'bar'})
        test.assert_equal(trans('foo'), 'bar')
        test.assert_equal(trans_lazy('foo'), 'bar')

    def test_localize(self):
        translator = self.get_translator()

        translator.add_translations('en', {
            'datetime': {
                'formats': {
                    'short': '%d.%M.%Y',
                },
            },
        })

        translator.add_formatter(self.format_datetime, ['datetime'])
        now = datetime.now()

        assert localize(now, 'short') == now.strftime('%d.%M.%Y')
        assert localize(now, '%d.%M.%Y') == now.strftime('%d.%M.%Y')

    @staticmethod
    def format_datetime(value, format, translator):
        format = translator.get_template('datetime.formats.' + format, default=format)
        return value.strftime(format)
