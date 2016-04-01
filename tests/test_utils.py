from langpack.utils import safe_format
from nose import tools as test


def test_safe_format():
    test.assert_equal(safe_format('Hello {name}!', name='John'), 'Hello John!')
    test.assert_equal(safe_format('Hello {name}!'), 'Hello {name}!')
    test.assert_equal(safe_format('Hello', name='John'), 'Hello')
