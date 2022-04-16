import unittest

from core.number.BigFloat import BigFloat


class BigFloatTestCase(unittest.TestCase):

    def test_should_store_number_string_as_big_float(self):
        bigfloat = BigFloat('1000000000.123456789012')
        self.assertEqual(bigfloat.number, 1000000000)
        self.assertEqual(bigfloat.fraction, 123456789012)

    def test_should_store_number_with_out_fraction_string_as_big_float(self):
        bigfloat = BigFloat('100')
        self.assertEqual(bigfloat.number, 100)
        self.assertEqual(bigfloat.fraction, 0)

    def test_should_store_large_number_as_big_float(self):
        bigfloat = BigFloat(1000000000, 123456789012)
        self.assertEqual(bigfloat.number, 1000000000)
        self.assertEqual(bigfloat.fraction, 123456789012)

    def test_should_to_string_as_combined_floating_point_number(self):
        bigfloat = BigFloat(1000000000, 123456789012)
        self.assertEqual(str(bigfloat), '1000000000.123456789012', 'separate numbers should be stringed')
        bigfloat = BigFloat('1000000000.123456789012')
        self.assertEqual(str(bigfloat), '1000000000.123456789012', 'stringed number should be stringed')

    def test_should_specify_to_string_delimiter(self):
        bigfloat = BigFloat(1000000000, 123456789012)
        self.assertEqual(bigfloat.stringify(':'), '1000000000:123456789012')

    def test_should_store_large_number_as_big_float_with_leading_fraction_zeros(self):
        bigfloat = BigFloat(1000000000, 12, 9)
        self.assertEqual(bigfloat.number, 1000000000)
        self.assertEqual(bigfloat.fraction, 12)
        self.assertEqual(bigfloat.fraction_leading_zeros, 9)

    def test_should_store_big_float_with_fraction_having_leading_zeros(self):
        bigfloat = BigFloat('0.000000000012')
        self.assertEqual(bigfloat.number, 0)
        self.assertEqual(bigfloat.fraction, 12)
        self.assertEqual(bigfloat.fraction_leading_zeros, 10)

    def test_should_to_string_combined_floating_point_number_with_leading_zeros(self):
        bigfloat = BigFloat(0, 12, 10)
        self.assertEqual(str(bigfloat), '0.000000000012', 'leading separate leading zero fraction')
        bigfloat = BigFloat('0.000000000012')
        self.assertEqual(str(bigfloat), '0.000000000012', 'stringed number should have leading zero fraction')


if __name__ == '__main__':
    unittest.main()
