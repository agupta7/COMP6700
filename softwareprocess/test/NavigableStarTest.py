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


    def test900_010_ExceptionNoStarName(self):
        with self.assertRaises(ValueError) as ctx:
            star = NS.NavigableStar(None)
        self.assertEquals(ctx.exception.args[0], self.strStarInvalid)

    def test900_020_ExceptionBlankStarName(self):
        with self.assertRaises(ValueError) as ctx:
            star = NS.NavigableStar("")
        self.assertEquals(ctx.exception.args[0], self.strStarInvalid)

    def test900_030_ExceptionWrongStarName(self):
        with self.assertRaises(ValueError) as ctx:
            star = NS.NavigableStar("asdf")
        self.assertEquals(ctx.exception.args[0], self.strStarInvalid)