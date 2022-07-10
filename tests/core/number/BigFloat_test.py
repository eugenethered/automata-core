import unittest

from core.number.BigFloat import BigFloat


class BigFloatTestCase(unittest.TestCase):

    def test_should_have_number_awareness(self):
        bigfloat = BigFloat('1000000000')
        self.assertEqual(bigfloat.number, 1000000000)
        self.assertEqual(bigfloat.decimals, 0)

    def test_should_have_decimal_awareness(self):
        bigfloat = BigFloat('0.000000000000000001')
        self.assertEqual(bigfloat.number, 1)
        self.assertEqual(bigfloat.decimals, 18)

    def test_should_have_number_and_decimal_awareness(self):
        bigfloat = BigFloat('1000000000.000000000000000001')
        self.assertEqual(bigfloat.number, 1000000000000000000000000001)
        self.assertEqual(bigfloat.decimals, 18)

    def test_should_have_negative_number_and_decimal_awareness(self):
        bigfloat = BigFloat('-1000000000.000000000000000001')
        self.assertEqual(bigfloat.number, -1000000000000000000000000001)
        self.assertEqual(bigfloat.decimals, 18)

    def test_should_represent_big_float_with_decimals(self):
        bigfloat = BigFloat('1000000000.000000000000000001')
        self.assertEqual(str(bigfloat), '1000000000.000000000000000001')

    def test_should_represent_negative_big_float_with_decimals(self):
        bigfloat = BigFloat('-1000000000.000000000000000001')
        self.assertEqual(str(bigfloat), '-1000000000.000000000000000001')

    def test_should_represent_big_float_without_decimals(self):
        bigfloat = BigFloat('1000000000')
        self.assertEqual(str(bigfloat), '1000000000.0')

    def test_should_represent_big_float_with_only_decimals(self):
        bigfloat = BigFloat('0.0025')
        self.assertEqual(str(bigfloat), '0.0025')

    def test_should_add(self):
        bigfloat = BigFloat('1000000000.000000000000000001')
        other = BigFloat('0.000000000000000001')
        result = bigfloat + other
        self.assertEqual(str(result), '1000000000.000000000000000002')

    def test_should_add_to_another_negative(self):
        bigfloat = BigFloat('1000000000.000000000000000001')
        other = BigFloat('-0.000000000000000001')
        result = bigfloat + other
        self.assertEqual(str(result), '1000000000.0')

    def test_should_add_negatives(self):
        bigfloat = BigFloat('-1000000000.000000000000000001')
        other = BigFloat('-0.000000000000000001')
        result = bigfloat + other
        self.assertEqual(str(result), '-1000000000.000000000000000002')

    def test_should_subtract(self):
        bigfloat = BigFloat('1000000000.000000000000000002')
        other = BigFloat('0.000000000000000001')
        result = bigfloat - other
        self.assertEqual(str(result), '1000000000.000000000000000001')

    def test_should_subtract_another_negative(self):
        bigfloat = BigFloat('0.000000000000000001')
        other = BigFloat('1000000000.000000000000000002')
        result = bigfloat - other
        self.assertEqual(str(result), '-1000000000.000000000000000001')

    def test_should_subtract_negatives(self):
        bigfloat = BigFloat('-1000000000.000000000000000001')
        other = BigFloat('-0.000000000000000001')
        result = bigfloat - other
        self.assertEqual(str(result), '-1000000000.0')

    def test_should_multiply(self):
        bigfloat = BigFloat('100000000000000000000000000.100000000000000000')
        other = BigFloat('0.000000000000000010')
        result = bigfloat * other
        self.assertEqual(str(result), '1000000000.000000000000000001')

    def test_should_divide(self):
        bigfloat = BigFloat('1000000000.000000000000000001')
        other = BigFloat('0.000000000000000010')
        result = bigfloat / other
        self.assertEqual(str(result), '100000000000000000000000000.1')

    def test_should_chop_remaining_zeros(self):
        bigfloat = BigFloat('100.000000000200000000')
        bigfloat.chop_zeros()
        self.assertEqual(str(bigfloat), '100.0000000002')

    def test_should_not_chop_remaining_zeros(self):
        bigfloat = BigFloat('100.000001000123')
        self.assertEqual(str(bigfloat), '100.000001000123')
        bigfloat.chop_zeros()
        self.assertEqual(str(bigfloat), '100.000001000123')

    def test_should_not_chop_remaining_zeros_from_whole_number(self):
        bigfloat = BigFloat('100')
        bigfloat.chop_zeros()
        self.assertEqual(str(bigfloat), '100.0')

    def test_should_compare_equality(self):
        bigfloat = BigFloat('100.0001000')
        other = BigFloat('100.0001')
        self.assertEqual(bigfloat, other)

    def test_should_crack_apart_numbers_and_decimals(self):
        bigfloat = BigFloat('1000000000.123456789012')
        (number_str, decimal_str) = bigfloat.crack()
        self.assertEqual(number_str, '1000000000')
        self.assertEqual(decimal_str, '123456789012')

    def test_should_crack_apart_numbers_and_decimals_with_zero_decimals(self):
        bigfloat = BigFloat('1000000000.0')
        (number_str, decimal_str) = bigfloat.crack()
        self.assertEqual(number_str, '1000000000')
        self.assertEqual(decimal_str, '0')

    def test_should_crack_apart_numbers_and_decimals_with_no_decimals(self):
        bigfloat = BigFloat('1000000000')
        (number_str, decimal_str) = bigfloat.crack()
        self.assertEqual(number_str, '1000000000')
        self.assertEqual(decimal_str, '0')

    def test_should_crack_apart_numbers_and_decimals_with_zero_numbers(self):
        bigfloat = BigFloat('0.123456789012')
        (number_str, decimal_str) = bigfloat.crack()
        self.assertEqual(number_str, '0')
        self.assertEqual(decimal_str, '123456789012')

    def test_should_crack_zeros(self):
        bigfloat = BigFloat('0.0')
        (number_str, decimal_str) = bigfloat.crack()
        self.assertEqual(number_str, '0')
        self.assertEqual(decimal_str, '0')

    def test_should_crack_zero(self):
        bigfloat = BigFloat('0')
        (number_str, decimal_str) = bigfloat.crack()
        self.assertEqual(number_str, '0')
        self.assertEqual(decimal_str, '0')


if __name__ == '__main__':
    unittest.main()
