import unittest
import softwareprocess.StarSighting as SS

class StarSightingTest(unittest.TestCase):
    def setUp(self):
        self.strDegreesBound = "Degrees should be an integer >= 0 and < 90."

    def tearDown(self):
        super(StarSightingTest, self).tearDown()
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
# ---- Unit tests
# ----