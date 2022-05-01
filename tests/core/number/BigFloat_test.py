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

    def test_should_verify_is_zero(self):
        bigfloat = BigFloat('0.00')
        self.assertTrue(bigfloat.is_zero())
        bigfloat = BigFloat('0')
        self.assertTrue(bigfloat.is_zero())
        bigfloat = BigFloat(0, 0)
        self.assertTrue(bigfloat.is_zero())
        bigfloat = BigFloat(0, 0, 0)
        self.assertTrue(bigfloat.is_zero())

    def test_should_whole_number_should_string_to_correct_places(self):
        bigfloat = BigFloat('100')
        self.assertEqual(bigfloat.number, 100)
        self.assertEqual(bigfloat.fraction, 0)
        self.assertEqual(bigfloat.fraction_leading_zeros, 0)
        self.assertEqual(str(bigfloat), '100.0')

    def test_should_zero_fraction_number_should_string_to_correct_places(self):
        bigfloat = BigFloat('100.00')
        self.assertEqual(bigfloat.number, 100)
        self.assertEqual(bigfloat.fraction, 0)
        self.assertEqual(bigfloat.fraction_leading_zeros, 1)
        self.assertEqual(str(bigfloat), '100.00')

    def test_should_without_zero_fraction_number_should_string_to_correct_places(self):
        bigfloat = BigFloat('100.12')
        self.assertEqual(bigfloat.number, 100)
        self.assertEqual(bigfloat.fraction, 12)
        self.assertEqual(bigfloat.fraction_leading_zeros, 0)
        self.assertEqual(str(bigfloat), '100.12')

    def test_should_with_multiple_zero_fraction_number_should_string_to_correct_places(self):
        bigfloat = BigFloat('100.00000012')
        self.assertEqual(bigfloat.number, 100)
        self.assertEqual(bigfloat.fraction, 12)
        self.assertEqual(bigfloat.fraction_leading_zeros, 6)
        self.assertEqual(str(bigfloat), '100.00000012')

    def test_should_not_sign(self):
        bigfloat = BigFloat('100.00')
        self.assertFalse(bigfloat.signed)
        self.assertEqual(str(bigfloat), '100.00')

    def test_should_sign(self):
        bigfloat = BigFloat('-100.00')
        self.assertTrue(bigfloat.signed)
        self.assertEqual(str(bigfloat), '-100.00')

    def test_should_have_float_less_than(self):
        self.assertTrue(BigFloat('100.0000000001') < BigFloat('100.0000000002'))
        self.assertTrue(BigFloat('100.0000000001') < BigFloat('100.0000000001'))
        self.assertTrue(BigFloat('100.0000000001') < BigFloat('200.0000000001'))
        self.assertFalse(BigFloat('100.0000000002') < BigFloat('100.0000000001'))
        self.assertFalse(BigFloat('200.0000000001') < BigFloat('100.0000000001'))


if __name__ == '__main__':
    unittest.main()
