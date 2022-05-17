import unittest

from core.number.BigFloat import BigFloat
from core.trade.Order import Order, OrderType, Status


class OrderTestCase(unittest.TestCase):

    def test_should_have_executed_order(self):
        order = Order('OTC', 'GBP', BigFloat('100.01'), '8888-8888', OrderType.MARKET, Status.EXECUTED, 1)
        self.assertEqual(order.instrument_from, 'OTC')
        self.assertEqual(order.instrument_to, 'GBP')
        self.assertEqual(order.quantity, BigFloat('100.01'))
        self.assertEqual(order.order_id, '8888-8888')
        self.assertEqual(order.order_type.value, 'market')
        self.assertEqual(order.status.value, 'executed')
        self.assertEqual(order.instant, 1)

    def test_should_have_executed_order_with_price(self):
        order = Order('OTC', 'GBP', BigFloat('100.01'), '8888-8888', OrderType.MARKET, Status.EXECUTED, 1, BigFloat('1.101'))
        self.assertEqual(order.instrument_from, 'OTC')
        self.assertEqual(order.instrument_to, 'GBP')
        self.assertEqual(order.quantity, BigFloat('100.01'))
        self.assertEqual(order.order_id, '8888-8888')
        self.assertEqual(order.order_type.value, 'market')
        self.assertEqual(order.status.value, 'executed')
        self.assertEqual(order.instant, 1)
        self.assertEqual(order.price, BigFloat('1.101'))

    def test_should_have_executed_order_with_value(self):
        order = Order('OTC', 'GBP', BigFloat('100.01'), '8888-8888', OrderType.MARKET, Status.EXECUTED, 1, BigFloat('1.101'), BigFloat('110.11101'))
        self.assertEqual(order.instrument_from, 'OTC')
        self.assertEqual(order.instrument_to, 'GBP')
        self.assertEqual(order.quantity, BigFloat('100.01'))
        self.assertEqual(order.order_id, '8888-8888')
        self.assertEqual(order.order_type.value, 'market')
        self.assertEqual(order.status.value, 'executed')
        self.assertEqual(order.instant, 1)
        self.assertEqual(order.price, BigFloat('1.101'))
        self.assertEqual(order.value, BigFloat('110.11101'))

    def test_should_parse_order_status(self):
        status = Status.parse('new')
        self.assertEqual(status, Status.NEW)

    def test_should_parse_order_type(self):
        order_type = OrderType.parse('market')
        self.assertEqual(order_type, OrderType.MARKET)


if __name__ == '__main__':
    unittest.main()
