import unittest
import softwareprocess.angles.Latitude as Lat

class LatitudeTest(unittest.TestCase):

    def setUp(self):
        self.latitudeTooLowStr = 'The latitude specified is too low!  It must be greater than -90 degrees and 0.0 minutes'
        self.latitudeTooHighStr = 'The latitude specified is too high!  It must be less than 90 degrees and 0.0 minutes'

    #-------
    #------ Will rely on AngleTest to validate basic scenarios.
    #------ The value Latitude class adds is it restricts the degree range to -90<lat<90
    #------ These will test that
    #------ Acceptance tests
    #------ 100 Constructor
    #------ Boundary value confidence
    #------ input : either number or string.  String is in format XdY.Y where X is number of degrees and Y.Y is number of minutes down to 1 /10 of a minute
    #------ output : instance of Latitude class
    #-----Happy path
    #-------degreeMinutesStr -> nominal value = '12d30.5'
    #-------degreeMinutesStr -> high value = '89d59.9'
    #-------degreeMinutesStr -> low value = '-89d59.9'
    #-------degreeMinutesFloat -> nominal value = 12.5
    #-------degreeMinutesFloat -> high value = 89.998
    #-------degreeMinutesFloat -> low value = -89.998
    #-----Sad path
    #-------degreeMinutesStr -> value too low = '-90d0.0'
    #-------degreeMinutesStr -> value too high = '90d0.0'

    def test100_010_ShouldConstructLatitudeNominal(self):
        alt = Lat.Latitude('12d30.5')
        self.assertIsInstance(alt, Lat.Latitude)
        self.assertEquals(alt.getDegreeMinuteString(), '12d30.5')
        self.assertAlmostEquals(alt.getDegreesFloat(), 12.5083, 3)
    def test100_020_ShouldConstructLatitudeHigh(self):
        alt = Lat.Latitude('89d59.9')
        self.assertIsInstance(alt, Lat.Latitude)
        self.assertEquals(alt.getDegreeMinuteString(), '89d59.9')
        self.assertAlmostEquals(alt.getDegreesFloat(), 89.9983, 3)
    def test100_030_ShouldConstructLatitudeLow(self):
        alt = Lat.Latitude('-89d59.9')
        self.assertIsInstance(alt, Lat.Latitude)
        self.assertEquals(alt.getDegreeMinuteString(), '-89d59.9')
        self.assertAlmostEquals(alt.getDegreesFloat(), -89.9983, 3)
    def test100_040_ShouldConstructLatitudeNominalFloat(self):
        alt = Lat.Latitude(12.5)
        self.assertIsInstance(alt, Lat.Latitude)
        self.assertEquals(alt.getDegreeMinuteString(), '12d30.0')
        self.assertAlmostEquals(alt.getDegreesFloat(), 12.5, 3)
    def test100_050_ShouldConstructLatitudeHighFloat(self):
        alt = Lat.Latitude(89.998)
        self.assertIsInstance(alt, Lat.Latitude)
        self.assertEquals(alt.getDegreeMinuteString(), '89d59.9')
        self.assertAlmostEquals(alt.getDegreesFloat(), 89.998, 3)
    def test100_060_ShouldConstructLatitudeLowFloat(self):
        alt = Lat.Latitude(-89.998)
        self.assertIsInstance(alt, Lat.Latitude)
        self.assertEquals(alt.getDegreeMinuteString(), '-89d59.9')
        self.assertAlmostEquals(alt.getDegreesFloat(), -89.998, 3)
