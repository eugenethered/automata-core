import unittest

from core.market.Market import Market


class MarketTestCase(unittest.TestCase):

    def test_should_obtain_market_from_value(self):
        value = 'binance'
        market = Market.parse(value)
        self.assertEqual(market, Market.BINANCE)

    def test_should_obtain_market_from_value_no_matter_the_case(self):
        value = 'bInaNce'
        market = Market.parse(value)
        self.assertEqual(market, Market.BINANCE)


if __name__ == '__main__':
    unittest.main()
