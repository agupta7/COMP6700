import unittest
import softwareprocess.StarSighting as SS

class StarSightingTest(unittest.TestCase):
    def setUp(self):
        self.strDegreesBound = "Degrees should be an integer >= 0 and < 90."
        self.strMinutesBound = "Minutes should be a decimal >= 0.0 and < 60.0."
        self.strHeightError = "Height should be a number >= 0.0"
        self.strTemperatureError = "Temperature should be an integer >= -20 & <= 120 in Farenheit"
        self.strPressureError = "Pressure should be an integer >= 100 & <= 1100 in millibars"
        self.selfHorizonError = "Horizon should be 'artificial' or 'natural'"

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
#                      degrees too low = -0.1
#
    def test200_010_ShouldSetHeightNominal(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setHeight(6.5)
        self.assertEquals(ss.getHeight(), 6.5)
    def test200_020_ShouldSetHeightLow(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setHeight(0.0)
        self.assertEquals(ss.getHeight(), 0)

    def test200_910_ShouldRaiseExceptionHeightNull(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setHeight(None)
        self.assertEquals(cxt.exception.args[0], self.strHeightError)
    def test200_920_ShouldRaiseExceptionHeightNotNumber(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setHeight('a')
        self.assertEquals(cxt.exception.args[0], self.strHeightError)
    def test200_930_ShouldRaiseExceptionHeightLow(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setHeight(-0.1)
        self.assertEquals(cxt.exception.args[0], self.strHeightError)

# ----300 setTemperature
# ----Boundary value confidence required
#   inputs :        temperature in farenheit ->     integer >= -20 & <= 120    mandatory, unvalidated
#   outputs :    instance of star sighting
# ----Happy path analysis
#           temperature -> nominal value = 70;
#           temperature -> low value = -20;
#           temperature -> high value = 120;
# ----Sad path analysis
#           height :   None temperature
#                       non-int temperature -> 98.6
#                      wrong temperature type = 'a'
#                      temperature too low = -21
#                      temperature too high = 121
#
    def test300_010_ShouldSetTemperatureNominal(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setTemperature(70)
        self.assertEquals(ss.getTemperature(), 70)
    def test300_020_ShouldSetTemperatureLow(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setTemperature(-20)
        self.assertEquals(ss.getTemperature(), -20)
    def test300_030_ShouldSetTemperatureHigh(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setTemperature(120)
        self.assertEquals(ss.getTemperature(), 120)

    def test300_910_ShouldRaiseExceptionTemperatureNull(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setTemperature(None)
        self.assertEquals(cxt.exception.args[0], self.strTemperatureError)
    def test300_920_ShouldRaiseExceptionTemperatureNonInt(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setTemperature(98.6)
        self.assertEquals(cxt.exception.args[0], self.strTemperatureError)
    def test300_930_ShouldRaiseExceptionTemperatureNotNumber(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setTemperature('a')
        self.assertEquals(cxt.exception.args[0], self.strTemperatureError)
    def test300_940_ShouldRaiseExceptionTemperatureLow(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setTemperature(-21)
        self.assertEquals(cxt.exception.args[0], self.strTemperatureError)
    def test300_950_ShouldRaiseExceptionTemperatureHigh(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setTemperature(121)
        self.assertEquals(cxt.exception.args[0], self.strTemperatureError)

# ----400 setPressure
# ----Boundary value confidence required
#   inputs :        pressure in farenheit ->     integer >= 100 & <= 1100    mandatory, unvalidated
#   outputs :    instance of star sighting
# ----Happy path analysis
#           pressure -> nominal value = 700;
#           pressure -> low value = 100;
#           pressure -> high value = 1100;
# ----Sad path analysis
#           height :   None pressure
#                       non-int pressure-> 198.6
#                      wrong pressure type = 'a'
#                      pressure too low = 99
#                      pressure too high = 1101
#
    def test400_010_ShouldSetPressureNominal(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setPressure(700)
        self.assertEquals(ss.getPressure(), 700)
    def test400_020_ShouldSetPressureLow(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setPressure(100)
        self.assertEquals(ss.getPressure(), 100)
    def test400_030_ShouldSetPressureHigh(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setPressure(1100)
        self.assertEquals(ss.getPressure(), 1100)

    def test400_910_ShouldRaiseExceptionPressureNull(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setPressure(None)
        self.assertEquals(cxt.exception.args[0], self.strPressureError)
    def test400_920_ShouldRaiseExceptionPressureNonInt(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setPressure(198.6)
        self.assertEquals(cxt.exception.args[0], self.strPressureError)
    def test400_930_ShouldRaiseExceptionPressureNotNumber(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setPressure('a')
        self.assertEquals(cxt.exception.args[0], self.strPressureError)
    def test400_940_ShouldRaiseExceptionPressureLow(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setPressure(99)
        self.assertEquals(cxt.exception.args[0], self.strPressureError)
    def test400_950_ShouldRaiseExceptionPressureHigh(self):
        ss = SS.StarSighting(20, 30.5)
        with self.assertRaises(ValueError) as cxt:
            ss.setPressure(1101)
        self.assertEquals(cxt.exception.args[0], self.strPressureError)


# ----500 setHorizon
# ----Boundary value confidence required
#   inputs :        horizon as string  ->  'natural' or 'artificial'- nothing else accepted
#   outputs :    instance of star sighting
# ----Happy path analysis
#           horizon -> nominal value = 'natural';
#           horizon -> boundary value = 'artificial';
# ----Sad path analysis
#           horizon:   None horizon
#                       non-str horizon-> 198.6
#                      any other string -> ''
#

    def test500_010_ShouldSetHorizonNominal(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setHorizon('natural')
        self.assertEquals(ss.getHorizon(), 'natural')
    def test500_020_ShouldSetHorizonNominal(self):
        ss = SS.StarSighting(20, 30.5)
        ss.setHorizon('artificial')
        self.assertEquals(ss.getHorizon(), 'artificial')

    def test500_910_ShouldRaiseExceptionNoneHorizon(self):
        pass
    def test500_920_ShouldRaiseExceptionNonStringHorizon(self):
        pass
    def test500_930_ShouldRaiseExceptionInvalidHorizon(self):
        pass
# ---- Unit tests
# ----