import pkg_resources
import unittest
import softwareprocess.NavigableStar as NS
import softwareprocess.test.NavigableStarTest as NST
import softwareprocess.test.AngleTest as AT
import softwareprocess.test.dispatchTest as dT
import softwareprocess.test.StarSightingTest as SST
import softwareprocess.test.SampleTest as ST
import softwareprocess.test.AltitudeTest as AltT

resource_package = __name__

str = pkg_resources.resource_string(resource_package, 'starLocations.cfg')

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(AT))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(AltT))
