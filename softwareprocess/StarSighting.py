import math

class StarSighting(object):
    def __init__(self, degrees, minutes):
        if not isinstance(degrees, (int, long)):
            
        self._degrees = degrees
        self._minutes = minutes

    def getDegrees(self):
        return self._degrees

    def getMinutes(self):
        return self._minutes