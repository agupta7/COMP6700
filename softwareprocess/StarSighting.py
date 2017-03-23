import math

class StarSighting(object):
    def __init__(self, degrees, minutes):
        strDegreesBound = "Degrees should be an integer >= 0 and < 90."
        strMinutesBound = "Minutes should be a decimal >= 0.0 and < 60.0."
        if not isinstance(degrees, (int, long)):
            raise ValueError(strDegreesBound)
        elif degrees < 0:
            raise ValueError(strDegreesBound)
        elif degrees >= 90:
            raise ValueError(strDegreesBound)

        if not isinstance(minutes, (int, long, float)):
            raise ValueError(strMinutesBound)
        elif minutes < 0:
            raise ValueError(strMinutesBound)
        elif minutes >= 60:
            raise ValueError(strMinutesBound)

        self._degrees = degrees
        self._minutes = minutes
        self._heightFt = 0
        self._temperatureK = 273 + (72 - 32) * 5/9
        self._pressureMillibar = 1010
        self._horizonNaturalArtificial = 0

    def getDegrees(self):
        return self._degrees
    def getMinutes(self):
        return self._minutes
    def setHeight(self, height):
        strHeightError = "Height should be a number >= 0.0"
        if not isinstance(height, (int, long, float)) or height < 0:
            raise ValueError(strHeightError)

        self._heightFt = height
        return self
    def getHeight(self):
        return self._heightFt