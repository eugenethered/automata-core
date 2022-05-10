import unittest

from core.transform.Ignore import Ignore


class IgnoreTestCase(unittest.TestCase):

    def test_should_set_ignore(self):
        ignore = Ignore(ignore=True)
        self.assertTrue(ignore.ignore)

    def test_should_not_set_ignore(self):
        ignore = Ignore(ignore=False)
        self.assertFalse(ignore.ignore)

    def test_should_be_ignored_by_default(self):
        ignore = Ignore()
        self.assertFalse(ignore.ignore)


if __name__ == '__main__':
    unittest.main()
