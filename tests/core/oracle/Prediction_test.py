import unittest

from core.number.BigFloat import BigFloat
from core.oracle.Prediction import Prediction


class PredictionTestCase(unittest.TestCase):

    def test_prediction_stringifies_trade(self):
        prediction = Prediction(['OTC', 'GBP'], BigFloat('10.0'))
        self.assertEqual("Prediction(outcome=['OTC', 'GBP'], profit=10.0, forced=False)", prediction.__str__())

    def test_prediction_stringifies_multi_trade(self):
        prediction = Prediction(['OTC', 'GBP', 'OTC'], BigFloat('10.0'))
        self.assertEqual("Prediction(outcome=['OTC', 'GBP', 'OTC'], profit=10.0, forced=False)", prediction.__str__())

    def test_forced_prediction(self):
        prediction = Prediction(['OTC', 'GBP'], BigFloat('10.0'), forced=True)
        self.assertEqual(prediction.outcome, ['OTC', 'GBP'])
        self.assertEqual(prediction.profit, BigFloat('10.0'))
        self.assertEqual(prediction.forced, True)


if __name__ == '__main__':
    unittest.main()
