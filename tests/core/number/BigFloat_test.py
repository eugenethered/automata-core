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

    def test_should_add_zero_based_big_floats(self):
        amount = BigFloat('0.00')
        other_amount = BigFloat('0.00')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('0.00'))

    def test_should_add_number_based_big_floats(self):
        amount = BigFloat('1.00')
        other_amount = BigFloat('1.00')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('2.00'))

    def test_should_add_fraction_based_big_floats(self):
        amount = BigFloat('0.01')
        other_amount = BigFloat('0.01')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('0.02'))

    def test_should_add_large_fraction_based_big_floats(self):
        amount = BigFloat('0.0100000001')
        other_amount = BigFloat('0.0100000001')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('0.0200000002'))

    def test_should_add_large_fraction_which_needs_padding(self):
        amount = BigFloat('0.000000001')
        other_amount = BigFloat('0.0000000001')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('0.0000000011'))

    def test_should_add_large_fraction_which_blows_to_next_fraction_unit(self):
        amount = BigFloat('0.0000000009')
        other_amount = BigFloat('0.0000000009')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('0.0000000018'))

    def test_should_add_large_fraction_which_blows_to_next_number_unit(self):
        amount = BigFloat('0.9')
        other_amount = BigFloat('0.9')
        result = amount.add(other_amount)
        self.assertEqual(result, BigFloat('1.8'))


if __name__ == '__main__':
    unittest.main()
