import unittest

from core.number.BigFloat import BigFloat
from core.oracle.Prediction import Prediction


class PredictionTestCase(unittest.TestCase):

    def test_prediction_stringifies_outcome(self):
        prediction = Prediction(['OTC', 'GBP'], BigFloat('10.0'))
        self.assertEqual("Prediction(outcome=['OTC', 'GBP'], percent=10.0, forced=False)", prediction.__str__())

    def test_prediction_stringifies_multiple_outcomes(self):
        prediction = Prediction(['OTC', 'GBP', 'OTC'], BigFloat('10.0'))
        self.assertEqual("Prediction(outcome=['OTC', 'GBP', 'OTC'], percent=10.0, forced=False)", prediction.__str__())

    def test_forced_prediction(self):
        prediction = Prediction(['OTC', 'GBP'], BigFloat('10.0'), forced=True)
        self.assertEqual(prediction.outcome, ['OTC', 'GBP'])
        self.assertEqual(prediction.percent, BigFloat('10.0'))
        self.assertEqual(prediction.forced, True)


if __name__ == '__main__':
    unittest.main()
