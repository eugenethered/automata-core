import unittest

from core.number.BigFloat import BigFloat
from core.position.Position import Position


class PositionTestCase(unittest.TestCase):

    def test_should_set_position_instrument_and_quantity(self):
        position = Position(instrument='GBP', quantity=BigFloat('1000.01'), instant=1)
        self.assertEqual(position.instrument, 'GBP')
        self.assertEqual(position.quantity, BigFloat('1000.01'))
        self.assertEqual(position.instant, 1)
        self.assertIsNone(position.exchanged_from)

    def test_should_set_exchanged_from(self):
        position = Position(instrument='GBP', quantity=BigFloat('1000.01'), instant=1, exchanged_from='OTC')
        self.assertEqual(position.instrument, 'GBP')
        self.assertEqual(position.quantity, BigFloat('1000.01'))
        self.assertEqual(position.instant, 1)
        self.assertEqual(position.exchanged_from, 'OTC')


if __name__ == '__main__':
    unittest.main()
