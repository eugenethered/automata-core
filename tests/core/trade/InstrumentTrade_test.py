import unittest

from core.number.BigFloat import BigFloat
from core.trade.InstrumentTrade import InstrumentTrade, Status, TradeMode


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

    def test_should_test_equality_on_instruments_status_and_order_id(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('101.01'), BigFloat('1.01'), BigFloat('102.0201'), status=Status.EXECUTED, order_id='8888-8888')
        other = InstrumentTrade('OTC', 'BTC', BigFloat('202.02'), BigFloat('2.02'), BigFloat('408.0804'), status=Status.EXECUTED, order_id='8888-8888')
        self.assertEqual(trade, other)

    def test_should_test_not_equal_when_order_id_is_different(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('101.01'), BigFloat('1.01'), BigFloat('102.0201'), status=Status.EXECUTED, order_id='1111-1111')
        other = InstrumentTrade('OTC', 'BTC', BigFloat('202.02'), BigFloat('2.02'), BigFloat('408.0804'), status=Status.EXECUTED, order_id='8888-8888')
        self.assertNotEqual(trade, other)

    def test_should_test_not_equal_when_status_is_different(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('101.01'), BigFloat('1.01'), BigFloat('102.0201'), status=Status.NEW, order_id='8888-8888')
        other = InstrumentTrade('OTC', 'BTC', BigFloat('202.02'), BigFloat('2.02'), BigFloat('408.0804'), status=Status.EXECUTED, order_id='8888-8888')
        self.assertNotEqual(trade, other)

    def test_instrument_trade_should_have_default_trade_mode(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('100'))
        self.assertEqual(trade.mode, TradeMode.TRADE)

    def test_instrument_trade_should_beset_to_predict_mode(self):
        trade = InstrumentTrade('OTC', 'BTC', BigFloat('100'))
        trade.mode = TradeMode.PREDICT
        self.assertEqual(trade.mode, TradeMode.PREDICT)

    def test_trading_mode_should_parse_correctly(self):
        trade_mode = TradeMode.parse('trade')
        self.assertEqual(trade_mode, TradeMode.TRADE)
        trade_mode_case = TradeMode.parse('pReDict')
        self.assertEqual(trade_mode_case, TradeMode.PREDICT)


if __name__ == '__main__':
    unittest.main()
