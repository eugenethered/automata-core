import unittest

from core.exchange.ExchangeRate import ExchangeRate
from core.number.BigFloat import BigFloat


class ExchangeRateTestCase(unittest.TestCase):

    def test_create_exchange_rate(self):
        exchange_rate = ExchangeRate(instrument='BTC', to_instrument='USDT', rate=BigFloat('38882.51'))
        self.assertEqual('BTC', exchange_rate.instrument)
        self.assertEqual('USDT', exchange_rate.to_instrument)
        self.assertEqual(BigFloat('38882.51'), exchange_rate.rate)

    def test_unpack_exchange_rate(self):
        (instrument, to_instrument, rate) = ExchangeRate('BTC', 'USDT', BigFloat('38882.51'))
        self.assertEqual('BTC', instrument)
        self.assertEqual('USDT', to_instrument)
        self.assertEqual(BigFloat('38882.51'), rate)

    def test_exchange_rate_inverse_rate(self):
        exchange_rate = ExchangeRate(instrument='BTC', to_instrument='USDT', rate=BigFloat('38882.51'))
        inverse_rate = exchange_rate.inverse()
        self.assertEqual(BigFloat('38882.51'), exchange_rate.rate)
        self.assertEqual(BigFloat('0.000025718504283802'), inverse_rate)

    def test_exchange_rate_inverse_rate_from_smaller(self):
        exchange_rate = ExchangeRate(instrument='USDT', to_instrument='BTC', rate=BigFloat('0.000025718504283802'))
        inverse_rate = exchange_rate.inverse()
        self.assertEqual(BigFloat('0.000025718504283802'), exchange_rate.rate)
        self.assertEqual(BigFloat('38882.510000001006939583'), inverse_rate)


if __name__ == '__main__':
    unittest.main()
