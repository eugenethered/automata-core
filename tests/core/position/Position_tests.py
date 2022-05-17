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

    def test_should_be_equal_when_instrument_exchanged_from_and_instant_are_equal(self):
        position = Position(instrument='GBP', quantity=BigFloat('1000.01'), instant=1, exchanged_from='OTC')
        other = Position(instrument='GBP', quantity=BigFloat('2000.02'), instant=1, exchanged_from='OTC')
        self.assertEqual(position, other)

    def test_should_not_be_equal_when_instrument_is_different(self):
        position = Position(instrument='BTC', quantity=BigFloat('1000.01'), instant=1, exchanged_from='OTC')
        other = Position(instrument='GBP', quantity=BigFloat('2000.02'), instant=1, exchanged_from='OTC')
        self.assertNotEqual(position, other)

    def test_should_not_be_equal_when_exchanged_from_is_different(self):
        position = Position(instrument='BTC', quantity=BigFloat('1000.01'), instant=1, exchanged_from='OTC')
        other = Position(instrument='BTC', quantity=BigFloat('2000.02'), instant=1, exchanged_from='GBP')
        self.assertNotEqual(position, other)

    def test_should_not_be_equal_when_instant_is_different(self):
        position = Position(instrument='BTC', quantity=BigFloat('1000.01'), instant=1, exchanged_from='OTC')
        other = Position(instrument='BTC', quantity=BigFloat('2000.02'), instant=2, exchanged_from='OTC')
        self.assertNotEqual(position, other)


if __name__ == '__main__':
    unittest.main()
