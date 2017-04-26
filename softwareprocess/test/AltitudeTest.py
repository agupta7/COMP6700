import unittest
import softwareprocess.angles.Altitude as Alt

class AltitudeTest(unittest.TestCase):

    def setUp(self):
        self.altitudeTooLowStr = 'The altitude specified is too low!  It must be greater than 0 degrees and 0.0 minutes'
        self.altitudeTooHighStr = 'The altitude specified is too high!  It must be less than 90 degrees and 0.0 minutes'

#-------
#------ Will rely on AngleTest to validate basic scenarios.
#------ The value Altitude class adds is it restricts the degree range to 0<alt<90
#------ These will test that
#------ Acceptance tests
#------ 100 Constructor
#------ Boundary value confidence
#------ input : either number or string.  String is in format XdY.Y where X is number of degrees and Y.Y is number of minutes down to 1 /10 of a minute
#------ output : instance of Altitude class
#-----Happy path
#-------degreeMinutesStr -> nominal value = '12d30.5'
#-------degreeMinutesStr -> high value = '89d59.9'
#-------degreeMinutesStr -> low value = '0d0.1'
#-------degreeMinutesFloat -> nominal value = 12.5
#-------degreeMinutesFloat -> high value = 89.999
#-------degreeMinutesFloat -> low value = 0.0016667
#-----Sad path
#-------degreeMinutesStr -> value too low = '0d0.0'
#-------degreeMinutesStr -> value too high = '90d0.0'

    def test100_010_ShouldConstructAltitudeNominal(self):
        alt = Alt.Altitude('12d30.5')
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '12d30.5')
        self.assertAlmostEquals(alt.getDegreesFloat(), 12.5083, 3)
    def test100_020_ShouldConstructAltitudeHigh(self):
        alt = Alt.Altitude('89d59.9')
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '89d59.9')
        self.assertAlmostEquals(alt.getDegreesFloat(), 89.9983, 3)
    def test100_030_ShouldConstructAltitudeLow(self):
        alt = Alt.Altitude('0d0.1')
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '0d0.1')
        self.assertAlmostEquals(alt.getDegreesFloat(), 0.0016667, 3)
    def test100_040_ShouldConstructAltitudeNominalFloat(self):
        alt = Alt.Altitude(12.5)
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '12d30.0')
        self.assertAlmostEquals(alt.getDegreesFloat(), 12.5, 3)
    def test100_050_ShouldConstructAltitudeHighFloat(self):
        alt = Alt.Altitude(89.998)
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '89d59.9')
        self.assertAlmostEquals(alt.getDegreesFloat(), 89.998, 3)
    def test100_060_ShouldConstructAltitudeLowFloat(self):
        alt = Alt.Altitude(0.001667)
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '0d0.1')
        self.assertAlmostEquals(alt.getDegreesFloat(), 0.001667, 3)

    def test100_910_ShouldRaiseErrorAltitudeTooLow(self):
        with self.assertRaises(ValueError) as ctx:
            alt = Alt.Altitude('0d0.0')
        self.assertEquals(ctx.exception.args[0], self.altitudeTooLowStr)
    def test100_910_ShouldRaiseErrorAltitudeTooLow(self):
        with self.assertRaises(ValueError) as ctx:
            alt = Alt.Altitude('90d0.0')
        self.assertEquals(ctx.exception.args[0], self.altitudeTooHighStr)