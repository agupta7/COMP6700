import json
from softwareprocess.convertString2Dictionary import convertString2Dictionary
import softwareprocess.test.SampleTest as ST
import unittest

# print(json.dumps(convertString2Dictionary("abc%3D12.3"), indent = 4))
# print(json.dumps(convertString2Dictionary("function%20%3D%20get_stars"), indent = 4))
# print(json.dumps(convertString2Dictionary("functi.on%3D%20calculatePosition%2C%20sighting%3DBetelgeuse"), indent = 4))
# print(json.dumps(convertString2Dictionary("key%3Dvalue%2C%20key%3Dvalue"), indent = 4))
# print(json.dumps(convertString2Dictionary("key%3D"), indent = 4))
# print(json.dumps(convertString2Dictionary("alue"), indent = 4))
# print(json.dumps(convertString2Dictionary("1key%3Dvalue"), indent = 4))
# print(json.dumps(convertString2Dictionary("k%20e%20y%20%3D%20value"), indent = 4))
# print(json.dumps(convertString2Dictionary(""), indent = 4))
# print(json.dumps(convertString2Dictionary("key1%3Dvalue%3B%20key2%3Dvalue"), indent = 4))

suite = unittest.TestLoader().loadTestsFromTestCase(ST.SampleTest)
unittest.TextTestRunner().run(suite)