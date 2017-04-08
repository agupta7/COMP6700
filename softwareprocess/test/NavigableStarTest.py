import unittest
import softwareprocess.NavigableStar as NS

class NavigableStarTest(unittest.TestCase):

    def setUp(self):
        self.strStarInvalid = "Please specify a valid navigable star in string insensitive format."
        self.strDateInvalidFormat = "Please specify the date in the format yyyy-mm-dd."
        self.strTimeInvalidFormat = "Please specify the time in the 24-hr format HH:MM:SS."

# ----------------------
# -----Acceptance tests
# -----100 Constructor
# -----input : String containing case insensitive navigable star's name
# -----output : an instance of navigable star
# --------Happy path analysis
#       starName : 'AlTaIr' nominal value
# ------ Sad path analysis
#       starName : None
#       starName : ''
#       starName : 'asdf'

    def test100_010_ShouldConstruct(self):
        star = NS.NavigableStar('AlTaIr')
        self.assertIsInstance(star, NS.NavigableStar)

    def test100_910_ExceptionNoStarName(self):
        with self.assertRaises(ValueError) as ctx:
            star = NS.NavigableStar(None)
        self.assertEquals(ctx.exception.args[0], self.strStarInvalid)

    def test100_920_ExceptionBlankStarName(self):
        with self.assertRaises(ValueError) as ctx:
            star = NS.NavigableStar("")
        self.assertEquals(ctx.exception.args[0], self.strStarInvalid)

    def test100_930_ExceptionWrongStarName(self):
        with self.assertRaises(ValueError) as ctx:
            star = NS.NavigableStar("asdf")
        self.assertEquals(ctx.exception.args[0], self.strStarInvalid)

# ----200 predict

    def test200_010ShouldPredict(self):
        star = NS.NavigableStar('Betelgeuse')
        latlong = star.predict("2016-01-17 03:15:42")
        self.assertEquals('75d53.6', latlong['long'])
        self.assertEquals('7d24.3', latlong['lat'])