from langpack.utils import safe_format, flatten_dict
from nose import tools as test


def test_safe_format():
    test.assert_equal(safe_format('Hello {name}!', name='John'), 'Hello John!')
    test.assert_equal(safe_format('Hello {name}!'), 'Hello {name}!')
    test.assert_equal(safe_format('Hello', name='John'), 'Hello')


def test_flatten_dict():
    data_dict = {
        'a': {
            'b': {
                'c': 'value',
            },
        },
        'd': {
            'e': 'value',
        },
        'f': 'value',
    }

    expected = {
        'a.b.c': 'value',
        'd.e': 'value',
        'f': 'value',
    }

    assert flatten_dict(data_dict) == expected
