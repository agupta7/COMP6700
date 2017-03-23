import math

class StarSighting(object):
    def __init__(self, degrees, minutes):
        strDegreesBound = "Degrees should be an integer >= 0 and < 90."
        if not isinstance(degrees, (int, long)):
            raise ValueError(strDegreesBound)
        elif degrees < 0:
            raise ValueError(strDegreesBound)

        self._degrees = degrees
        self._minutes = minutes

    def getDegrees(self):
        return self._degrees

    def getMinutes(self):
        return self._minutes