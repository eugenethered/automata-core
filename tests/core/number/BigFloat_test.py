import unittest

from core.number.BigFloat import BigFloat


class BigFloatTestCase(unittest.TestCase):

    def test_should_store_number_string_as_big_float(self):
        bigfloat = BigFloat('1000000000.123456789012')
        self.assertEqual(bigfloat.number, 1000000000)
        self.assertEqual(bigfloat.fraction, 123456789012)

    def test_should_store_large_number_as_big_float(self):
        bigfloat = BigFloat(1000000000, 123456789012)
        self.assertEqual(bigfloat.number, 1000000000)
        self.assertEqual(bigfloat.fraction, 123456789012)

    def test_should_to_string_as_combined_floating_point_number(self):
        bigfloat = BigFloat(1000000000, 123456789012)
        self.assertEqual(str(bigfloat), '1000000000.123456789012', 'separate numbers should be stringed')
        bigfloat = BigFloat('1000000000.123456789012')
        self.assertEqual(str(bigfloat), '1000000000.123456789012', 'stringed number should be stringed')


if __name__ == '__main__':
    unittest.main()
