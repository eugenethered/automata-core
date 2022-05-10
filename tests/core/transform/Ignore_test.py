import unittest
from dataclasses import dataclass

from core.transform.Ignore import Ignore


class IgnoreTestCase(unittest.TestCase):

    def test_should_set_ignore(self):
        ignore = Ignore()
        ignore.ignore = True
        self.assertTrue(ignore.ignore)

    def test_should_not_set_ignore(self):
        ignore = Ignore()
        ignore.ignore = False
        self.assertFalse(ignore.ignore)

    def test_should_be_ignored_by_default(self):
        ignore = Ignore()
        self.assertFalse(ignore.ignore)

    def test_should_inherit_with_default(self):
        @dataclass
        class TestIgnore(Ignore):
            value: str
        ignore = TestIgnore(value='test')
        self.assertEqual(ignore.value, 'test')
        self.assertFalse(ignore.ignore)

    def test_should_inherit_with_setting_ignore(self):
        @dataclass
        class TestIgnore(Ignore):
            value: str
        ignore = TestIgnore(value='test')
        ignore.ignore = True
        self.assertEqual(ignore.value, 'test')
        self.assertTrue(ignore.ignore)


if __name__ == '__main__':
    unittest.main()
