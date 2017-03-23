import unittest
import softwareprocess.dispatch as dispatch

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