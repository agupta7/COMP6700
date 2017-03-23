import unittest
import softwareprocess.StarSighting as SS

class StarSightingTest(unittest.TestCase):
    def setUp(self):
        self.strDegreesBound = "Degrees should be an integer >= 0 and < 90."
        self.strMinutesBound = "Minutes should be a decimal >= 0.0 and < 60.0."

    def tearDown(self):
        pass


# -----------------------------------------
# ---------- Acceptance tests
# ----100 constructor
# ----Boundary value confidence required
#   inputs :        degrees ->      integer >= 0 & < 90     mandatory, unvalidated
#                   minutes ->      numeric >= 0.0 & < 60   mandatory, unvalidated
#   outputs :    instance of star sighting
# ----Happy path analysis
#           degrees -> nominal value = 20; minutes -> nominal value = 30
#           degrees -> low value = 0; minutes -> nominal value = 30
#           degrees -> high value = 89; minutes -> nominal value = 30
#           degrees -> nominal value = 20; minutes -> low value = 0.0
#           degrees -> nominal value = 20; minutes -> high value = 59.9
# ----Sad path analysis
#           degrees :   non-int degrees = 55.5
#                       None degrees
#                       wrong degrees type = 'a'
#                       degrees too low = -1
#                       degrees too high = 90
#           minutes :   non-numeric minutes = 'b'
#                       None minutes
#                       minutes too low = -0.1
#                       minutes too high = 60
#
    def test100_010_ShouldConstructNominalValues(self):
        ss = SS.StarSighting(20, 30.0)
        self.assertIsInstance(ss, SS.StarSighting)
        self.assertEquals(ss.getDegrees(), 20)
        self.assertEquals(ss.getMinutes(), 30.0)
    def test100_020_ShouldConstructLowDegrees(self):
        ss = SS.StarSighting(0, 30.0)
        self.assertIsInstance(ss, SS.StarSighting)
        self.assertEquals(ss.getDegrees(), 0)
        self.assertEquals(ss.getMinutes(), 30.0)
    def test100_030_ShouldConstructHighDegrees(self):
        ss = SS.StarSighting(89, 30.0)
        self.assertIsInstance(ss, SS.StarSighting)
        self.assertEquals(ss.getDegrees(), 89)
        self.assertEquals(ss.getMinutes(), 30.0)
    def test100_040_ShouldConstructLowMinutes(self):
        ss = SS.StarSighting(20, 0.0)
        self.assertIsInstance(ss, SS.StarSighting)
        self.assertEquals(ss.getDegrees(), 20)
        self.assertEquals(ss.getMinutes(), 0.0)
    def test100_050_ShouldConstructHighMinutes(self):
        ss = SS.StarSighting(20, 59.9)
        self.assertIsInstance(ss, SS.StarSighting)
        self.assertEquals(ss.getDegrees(), 20)
        self.assertEquals(ss.getMinutes(), 59.9)

    def test100_810_ShouldRaiseExceptionNonIntDegrees(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(20.5, 30.0)
        self.assertEquals(cxt.exception.args[0], self.strDegreesBound)
    def test100_810_ShouldRaiseExceptionNullDegrees(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(None, 30.0)
        self.assertEquals(cxt.exception.args[0], self.strDegreesBound)
    def test100_820_ShouldRaiseExceptionWrongTypeDegrees(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting('a', 30.0)
        self.assertEquals(cxt.exception.args[0], self.strDegreesBound)
    def test100_830_ShouldRaiseExceptionDegreesLow(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(-1, 30.0)
        self.assertEquals(cxt.exception.args[0], self.strDegreesBound)
    def test100_840_ShouldRaiseExceptionDegreesHigh(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(90, 30.0)
        self.assertEquals(cxt.exception.args[0], self.strDegreesBound)

    def test100_910_ShouldRaiseExceptionNonNumberMinutes(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(20, 'a')
        self.assertEquals(cxt.exception.args[0], self.strMinutesBound)
    def test100_920_ShouldRaiseExceptionNullMinutes(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(20, None)
        self.assertEquals(cxt.exception.args[0], self.strMinutesBound)
    def test100_930_ShouldRaiseExceptionMinutesLow(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(20, -0.1)
        self.assertEquals(cxt.exception.args[0], self.strMinutesBound)
    def test100_940_ShouldRaiseExceptionMinutesHigh(self):
        with self.assertRaises(ValueError) as cxt:
            ss = SS.StarSighting(20, 60)
        self.assertEquals(cxt.exception.args[0], self.strMinutesBound)


# ----200 setHeight
# ----Boundary value confidence required
#   inputs :        height in ft ->     numeric >= 0    mandatory, unvalidated
#   outputs :    instance of star sighting
# ----Happy path analysis
#           height -> nominal value = 6.5;
#           height -> low value = 0;
# ----Sad path analysis
#           height :   None height
#                      wrong height type = 'a'
#                      degrees too low = -1
#
    def test200_010_ShouldSetHeightNominal(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setHeight(6.5)
        self.assertEquals(ss.getHeight(), 6.5)
# ---- Unit tests
# ----