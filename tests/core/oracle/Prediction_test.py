import unittest

from core.number.BigFloat import BigFloat
from core.oracle.Prediction import Prediction


class PredictionTestCase(unittest.TestCase):

    def test_prediction_stringifies_trade(self):
        prediction = Prediction(['BTC', 'USDT'], BigFloat('10.0'))
        self.assertEqual("Prediction(outcome=['BTC', 'USDT'], profit=10.0)", prediction.__str__())

    def test_prediction_stringifies_multi_trade(self):
        prediction = Prediction(['BTC', 'USDT', 'ETH'], BigFloat('10.0'))
        self.assertEqual("Prediction(outcome=['BTC', 'USDT', 'ETH'], profit=10.0)", prediction.__str__())


if __name__ == '__main__':
    unittest.main()
