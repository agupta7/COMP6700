import unittest

import softwareprocess.prod.dispatch as dispatch


class DispatchTest(unittest.TestCase):

# Acceptance tests
#--- test cases enumerated in Excel sheet 201720Assignment4

    def test100_010_DispatchAdjust(self):
        dict = dispatch.dispatch({'op': 'adjust'})
        self.assertEquals(dict['op'], 'adjust')
    def test100_020_DispatchPredict(self):
        dict = dispatch.dispatch({'op': 'predict'})
        self.assertEquals(dict['op'], 'predict')
    def test100_020_DispatchCorrect(self):
        dict = dispatch.dispatch({'op': 'correct'})
        self.assertEquals(dict['op'], 'correct')
    def test100_020_DispatchLocate(self):
        dict = dispatch.dispatch({'op': 'locate'})
        self.assertEquals(dict['op'], 'locate')

    def test100_910_DispatchInvalidOp(self):
        dict = dispatch.dispatch({'op': 'beam me up'})
        self.assertEquals(dict['error'], 'op is not a legal operation')
        self.assertEquals(dict['op'], 'beam me up')
    def test100_920_DispatchNoOp(self):
        dict = dispatch.dispatch({'observation': '40d42'})
        self.assertEquals(dict['observation'], '40d42')
        self.assertEquals(dict['error'], 'no op  is specified')
    def test100_020_DispatchNoDict(self):
        dict = dispatch.dispatch(12)
        self.assertEquals(dict['error'], 'parameter is not a dictionary')
    def test100_940_DispatchNone(self):
        dict = dispatch.dispatch(None)
        self.assertEquals(dict['error'], 'parameter is missing')


    def test200_010Calculation(self):
        dict = dispatch.dispatch({'op': 'adjust', 'observation': '7d13.3'})
        self.assertEquals('7d6.0', dict['altitude'])
    def test200_020Calculation(self):
        dict = dispatch.dispatch({'op': 'adjust', 'observation': '7d13.3', 'height': '100'})
        self.assertEquals('6d56.3', dict['altitude'])
    def test200_030Calculation(self):
        dict = dispatch.dispatch({'op': 'adjust', 'observation': '7d13.3', 'temperature': '60'})
        self.assertEquals('7d5.8', dict['altitude'])
    def test200_040Calculation(self):
        dict = dispatch.dispatch({'op': 'adjust', 'observation': '7d13.3', 'temperature': '60', 'pressure': '900'})
        self.assertEquals('7d6.6', dict['altitude'])
    def test200_050Calculation(self):
        dict = dispatch.dispatch({'op': 'adjust', 'observation': '7d13.3', 'temperature': '60', 'pressure': '900', 'horizon': 'artificial'})
        self.assertEquals('7d6.6', dict['altitude'])
    def test200_910CalculationErrorObservationMissing(self):
        dict = dispatch.dispatch({'op': 'adjust'})
        self.assertEquals('mandatory information is missing', dict['error'])
    def test200_920CalculationErrorObservationInvalid(self):
        dict = dispatch.dispatch({'op': 'adjust', 'observation': '12.65'})
        self.assertEquals('observation is invalid', dict['error'])

    def test300_010Predict(self):
        dict = dispatch.dispatch({'op': 'predict', 'body': 'AlTaIr'})
        self.assertIn("lat", dict)
        self.assertIn("long", dict)

    def test300_020Predict(self):
        dict = dispatch.dispatch({'op': 'predict', 'body': 'AlTaIr', 'date': '2017-04-01'})
        self.assertIn("lat", dict)
        self.assertIn("long", dict)

    def test300_020Predict(self):
        dict = dispatch.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'})
        self.assertEquals("7d24.3", dict['lat'])
        self.assertEquals("75d53.6", dict['long'])

    def test300_910PredictWrongDate(self):
        dict = dispatch.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-175'})
        self.assertIn("error", dict)

    def test300_920PredictWrongDate(self):
        dict = dispatch.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': ''})
        self.assertIn("error", dict)

    def test300_930PredictWrongTime(self):
        dict = dispatch.dispatch({'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:60:23'})
        self.assertIn("error", dict)