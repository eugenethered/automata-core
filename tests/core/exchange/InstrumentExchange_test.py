import unittest

from core.exchange.InstrumentExchange import InstrumentExchange


class InstrumentExchangeTestCase(unittest.TestCase):

    def test_create_instrument_exchange(self):
        instrument_exchange = InstrumentExchange(instrument='OTC', to_instrument='BTC')
        self.assertEqual('OTC', instrument_exchange.instrument)
        self.assertEqual('BTC', instrument_exchange.to_instrument)

    def test_unpack_instrument_exchange(self):
        (instrument, to_instrument) = InstrumentExchange('OTC', 'BTC')
        self.assertEqual('OTC', instrument)
        self.assertEqual('BTC', to_instrument)

    def test_stringify_instrument_exchange(self):
        instrument_exchange = InstrumentExchange('OTC', 'BTC')
        self.assertEqual('OTC/BTC', str(instrument_exchange))

    def test_should_invert_exchange_as_new_entity(self):
        instrument_exchange = InstrumentExchange('OTC', 'BTC')
        inverted_instrument_exchange = instrument_exchange.invert()
        self.assertEqual('BTC/OTC', str(inverted_instrument_exchange))

    def test_update_instrument_exchange_with_precision(self):
        instrument_exchange = InstrumentExchange(instrument='OTC', to_instrument='BTC')
        self.assertEqual('OTC', instrument_exchange.instrument)
        self.assertEqual('BTC', instrument_exchange.to_instrument)


if __name__ == '__main__':
    unittest.main()
