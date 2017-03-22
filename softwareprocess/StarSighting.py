import math

class StarSighting(object):
    def __init__(self, degrees, minutes):
        self._degrees = degrees
        self._minutes = minutes

    def getDegrees(self):
        return self._degrees

    def getMintues(self):
        return self._minutes