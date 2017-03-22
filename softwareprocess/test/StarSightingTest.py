import unittest
import softwareprocess.StarSighting as SS

class StarSightingTest(unittest.TestCase):
    def setUp(self):
        super(StarSightingTest, self).setUp()
        pass

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

        pass

    def test100_910_ShouldRaiseExceptionNonIntDegrees(self):
        pass

# ---- Unit tests
# ----