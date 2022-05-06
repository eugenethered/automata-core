import unittest

from core.number.BigFloat import BigFloat
from core.trade.Order import Order, OrderType, Status


class OrderTestCase(unittest.TestCase):

    def test_should_have_executed_order(self):
        order = Order('OTC', 'GBP', BigFloat('100.01'), '8888-8888', OrderType.MARKET, Status.EXECUTED)
        self.assertEqual(order.instrument_from, 'OTC')
        self.assertEqual(order.instrument_to, 'GBP')
        self.assertEqual(order.quantity, BigFloat('100.01'))
        self.assertEqual(order.order_id, '8888-8888')
        self.assertEqual(order.order_type.value, 'market')
        self.assertEqual(order.status.value, 'executed')


if __name__ == '__main__':
    unittest.main()
