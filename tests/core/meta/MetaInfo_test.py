import unittest

from core.meta.MetaInfo import MetaInfo
from core.meta.exception.SetupFileNotFoundError import SetupFileNotFoundError


class MetaInfoTestCase(unittest.TestCase):

    def setUp(self):
        self.test_default_path = '../../../'

    def test_should_have_setup_file(self):
        meta_info = MetaInfo(default_path=self.test_default_path)
        self.assertTrue(meta_info.setup_file_exists())

    def test_should_not_find_setup_file_using_default_path(self):
        with self.assertRaises(SetupFileNotFoundError):
            MetaInfo()

    def test_should_get_version_from_setup(self):
        meta_info = MetaInfo(default_path=self.test_default_path)
        result = meta_info.get_version()
        self.assertRegex(result, r'\d\.\d\.\d')

    def test_should_get_description_from_setup(self):
        meta_info = MetaInfo(default_path=self.test_default_path)
        result = meta_info.get_description()
        self.assertEqual(result, 'Automata Core', 'Using actual description so check setup.cfg file')


if __name__ == '__main__':
    unittest.main()
