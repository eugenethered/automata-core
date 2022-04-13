import unittest

from core.trade.InstrumentTrade import InstrumentTrade


class InstrumentTradeTestCase(unittest.TestCase):

    def test_should_have_two_instruments_of_quantity_to_trade(self):
        trade = InstrumentTrade('USDT', 'BTC', 100)
        self.assertEqual('USDT', trade.instrument_from)
        self.assertEqual('BTC', trade.instrument_to)
        self.assertEqual(100, trade.quantity)

    def test_should_have_instruments_to_trade_with_fractional_quanities(self):
        trade = InstrumentTrade('BTC', 'USDT', 0.0025)
        self.assertEqual('BTC', trade.instrument_from)
        self.assertEqual('USDT', trade.instrument_to)
        self.assertEqual(0.0025, trade.quantity)


if __name__ == '__main__':
    unittest.main()
