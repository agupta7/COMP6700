import unittest
import softwareprocess.angles.Longitude as Long

class LongitudeTest(unittest.TestCase):

    def setUp(self):
        self.longitudeTooLowStr = 'The longitude specified is too low!  It must be greater than or equal to 0 degrees and 0.0 minutes'
        self.longitudeTooHighStr = 'The longitude specified is too high!  It must be less than 360 degrees and 0.0 minutes'

    #-------
    #------ Will rely on AngleTest to validate basic scenarios.
    #------ The value Longitude class adds is it restricts the degree range to 0<=long<90
    #------ These will test that
    #------ Acceptance tests
    #------ 100 Constructor
    #------ Boundary value confidence
    #------ input : either number or string.  String is in format XdY.Y where X is number of degrees and Y.Y is number of minutes down to 1 /10 of a minute
    #------ output : instance of Longitude class
    #-----Happy path
    #-------degreeMinutesStr -> nominal value = '12d30.5'
    #-------degreeMinutesStr -> high value = '89d59.9'
    #-------degreeMinutesStr -> low value = '0d0.0'
    #-------degreeMinutesFloat -> nominal value = 12.5
    #-------degreeMinutesFloat -> high value = 89.998
    #-------degreeMinutesFloat -> low value = 0
    #-----Sad path
    #-------degreeMinutesStr -> value too low = '-0d0.1'
    #-------degreeMinutesStr -> value too high = '90d0.0'
        
    def test100_010_ShouldConstructLongitudeNominal(self):
        long = Long.Longitude('12d30.5')
        self.assertIsInstance(long, Long.Longitude)
        self.assertEquals(long.getDegreeMinuteString(), '12d30.5')
        self.assertAlmostEquals(long.getDegreesFloat(), 12.5083, 3)
    def test100_020_ShouldConstructLongitudeHigh(self):
        long = Long.Longitude('359d59.9')
        self.assertIsInstance(long, Long.Longitude)
        self.assertEquals(long.getDegreeMinuteString(), '359d59.9')
        self.assertAlmostEquals(long.getDegreesFloat(), 359.9983, 3)
    def test100_030_ShouldConstructLongitudeLow(self):
        long = Long.Longitude('0d0.0')
        self.assertIsInstance(long, Long.Longitude)
        self.assertEquals(long.getDegreeMinuteString(), '0d0.0')
        self.assertEquals(long.getDegreesFloat(), 0)
    def test100_040_ShouldConstructLongitudeNominalFloat(self):
        long = Long.Longitude(12.5)
        self.assertIsInstance(long, Long.Longitude)
        self.assertEquals(long.getDegreeMinuteString(), '12d30.0')
        self.assertEquals(long.getDegreesFloat(), 12.5, 3)
    def test100_050_ShouldConstructLongitudeHighFloat(self):
        long = Long.Longitude(359.998)
        self.assertIsInstance(long, Long.Longitude)
        self.assertEquals(long.getDegreeMinuteString(), '359d59.9')
        self.assertAlmostEquals(long.getDegreesFloat(), 359.998, 3)
    def test100_060_ShouldConstructLongitudeLowFloat(self):
        long = Long.Longitude(0)
        self.assertIsInstance(long, Long.Longitude)
        self.assertEquals(long.getDegreeMinuteString(), '0d0.0')
        self.assertEquals(long.getDegreesFloat(), 0)
        
    def test100_910_ShouldRaiseErrorLongitudeTooLow(self):
        with self.assertRaises(ValueError) as ctx:
            long = Long.Longitude('-0d0.1')
        self.assertEquals(ctx.exception.args[0], self.longitudeTooLowStr)

    def test100_920_ShouldRaiseErrorLongitudeTooHigh(self):
        with self.assertRaises(ValueError) as ctx:
            long = Long.Longitude('3600d0.0')
        self.assertEquals(ctx.exception.args[0], self.longitudeTooHighStr)