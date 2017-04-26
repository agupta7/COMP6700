import pkg_resources
import unittest
import softwareprocess.NavigableStar as NS
import softwareprocess.test.NavigableStarTest as NST
import softwareprocess.test.AngleTest as AT
import softwareprocess.test.dispatchTest as dT
import softwareprocess.test.StarSightingTest as SST
import softwareprocess.test.SampleTest as ST

resource_package = __name__

str = pkg_resources.resource_string(resource_package, 'starLocations.cfg')

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(ST))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(SST))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(dT))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(AT))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromModule(NST))
