import unittest
import softwareprocess.Angle as A

class AngleTest(unittest.TestCase):

    def setUp(self):
        self.strDegreesFormatError = "String should in format XdY.Y where X is degrees and Y.Y is floating point minutes"

# ---------
# ----Acceptance tests
# ----100 Constructor
# ----Boundary value confidence
# ----input : string containing the degrees and minutes in the form XdY.Y for X is degrees Y.Y is minutes
# ----output : an instance of Angle
# ----Happy path analysis:
#       degreeMinutesStr -> nominal value = 50d30.9
#       degreeMinutesStr -> low value = -10d0.0
#       degreeMinutesStr -> high value = 999d59.9
# ---Sad path analysis
#       degreeMinutesStr -> None / not specified
#       degreeMinutesStr -> 12 (an integer)
#       degreeMinutesStr -> '' empty string
#       degreeMinutesStr -> '0d60.0' minutes is too high
#       degreeMinutesStr -> '0d-0.1' minutes is too low
#       degreeMintuesStr -> '0.5d10.0' degrees is non integer
#       degreeMinutesStr -> '1ad10.0' wrong format
#       degreeMintuesStr -> '12d1' minutes must have decimal
#       degreeMinutesStr -> '12d12.0m' minutes in the wrong format

    def test100_010_ShouldConstructAngle(self):
        angle = A.Angle('50d30.9')
        self.assertIsInstance(angle, A.Angle)
        self.assertEquals(angle.getDegrees(), 50)
        self.assertEquals(angle.getMinutes(), 30.9)

    def test100_020_ShouldConstructAngleLow(self):
        angle = A.Angle('-10d0.0')
        self.assertIsInstance(angle, A.Angle)
        self.assertEquals(angle.getDegrees(), -10)
        self.assertEquals(angle.getMinutes(), 0)

    def test100_030_ShouldConstructAngleHigh(self):
        angle = A.Angle('999d59.9')
        self.assertIsInstance(angle, A.Angle)
        self.assertEquals(angle.getDegrees(), 999)
        self.assertEquals(angle.getMinutes(), 59.9)

    def test900_010_ShouldErrorNoneAngle(self):
        with self.assertRaises(ValueError) as ctx:
            angle = A.Angle(None)
        self.assertEquals(ctx.exception.args[0], self.strDegreesFormatError)

    def test900_020_ExceptionIntegerAngle(self):
        with self.assertRaises(ValueError) as ctx:
            angle = A.Angle(None)
        self.assertEquals(ctx.exception.args[0], self.strDegreesFormatError)

    def test900_030_ExceptionBlankAngle(self):
        with self.assertRaises(ValueError) as ctx:
            angle = A.Angle('')
        self.assertEquals(ctx.exception.args[0], self.strDegreesFormatError)

    def test900_040_ExceptionMinutesHigh(self):
        with self.assertRaises(ValueError) as ctx:
            angle = A.Angle('0d60.0')
        self.assertEquals(ctx.exception.args[0], self.strDegreesFormatError)