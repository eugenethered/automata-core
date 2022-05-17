import unittest

from core.number.BigFloat import BigFloat
from core.trade.InstrumentTrade import InstrumentTrade, Status


class InstrumentTradeTestCase(unittest.TestCase):

    def test_should_have_two_instruments_of_quantity_to_trade(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('100'))
        self.assertEqual('OTC', trade.instrument_from)
        self.assertEqual('BTC', trade.instrument_to)
        self.assertEqual('100.0', trade.quantity)
        self.assertEqual(None, trade.instant)

    def test_should_have_instruments_to_trade_with_fractional_quantity(self):
        trade = InstrumentTrade('BTC', 'OTC', BigFloat('0.0025'))
        self.assertEqual('BTC', trade.instrument_from)
        self.assertEqual('OTC', trade.instrument_to)
        self.assertEqual('0.0025', trade.quantity)

    def test_should_have_price(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('101.01'), BigFloat('1.01'))
        self.assertEqual('OTC', trade.instrument_from)
        self.assertEqual('BTC', trade.instrument_to)
        self.assertEqual('101.01', trade.quantity)
        self.assertEqual('1.01', trade.price)

    def test_should_have_value(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('101.01'), BigFloat('1.01'), BigFloat('102.0201'))
        self.assertEqual('OTC', trade.instrument_from)
        self.assertEqual('BTC', trade.instrument_to)
        self.assertEqual('102.0201', trade.value)

    def test_should_have_new_status_and_no_description_for_trade(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('100'))
        self.assertEqual('new', trade.status.value)
        self.assertEqual(None, trade.description)

    def test_should_have_set_status_and_description_for_trade(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('100'))
        trade.status = Status.EXECUTED
        trade.description = '27'
        trade.instant = 1
        self.assertEqual('executed', trade.status.value)
        self.assertEqual('27', trade.description)
        self.assertEqual(1, trade.instant)


if __name__ == '__main__':
    unittest.main()
