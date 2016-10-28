from langpack.formatters import format_datetime
from langpack.translators import NOT_RPOVIDED
from langpack.utils import flatten_dict
from datetime import datetime


class TranslatorMock:
    def __init__(self, initial={}):
        self._translations = flatten_dict(initial)

    def get_template(self, str_path, default=NOT_RPOVIDED):
        return self._translations.get(str_path, default)


def test_format_datetime():
    translator = TranslatorMock({
        'datetime': {
            'formats': {
                'short': '%d.%m.%Y',
                'full': '%-d %B %Y г.',
            },
            'day_names': ['~', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
            'short_day_names': ['~', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
            'month_names': ['~', 'Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря'],
            'short_month_names': ['~', 'Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
        },
    })

    today = datetime(2016, 1, 1, 18, 30)
    assert format_datetime(today, 'short', translator) == '01.01.2016'
    assert format_datetime(today, 'full', translator) == '1 Января 2016 г.'
    assert format_datetime(today, '%A %-d %B %Y г.', translator) == 'Пятница 1 Января 2016 г.'
    assert format_datetime(today, '%a %-d %b %Y г.', translator) == 'Пт 1 Янв 2016 г.'
