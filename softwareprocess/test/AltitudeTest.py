import unittest
import softwareprocess.angles.Altitude as Alt

class AltitudeTest(unittest.TestCase):

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
#-------degreeMinutesFloat -> high value = '89.999'
#-------degreeMinutesFloat -> low value = '0.0016667'
#-----Sad path
#-------degreeMinutesStr -> value too low = '0d0.0'
#-------degreeMinutesStr -> value too high = '90d0.0'

    def test100_010_ShouldConstructAltitude(self):
        alt = Alt.Altitude('12d30.5')
        self.assertIsInstance(alt, Alt.Altitude)
        self.assertEquals(alt.getDegreeMinuteString(), '12d30.5')