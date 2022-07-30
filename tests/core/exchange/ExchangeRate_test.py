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


if __name__ == '__main__':
    unittest.main()
