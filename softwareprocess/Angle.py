
class Angle:

    def __init__(self, degStr):
        strDegreesMinutesFormatError = "String should in format XdY.Y where X is degrees and Y.Y is floating point minutes"

        if not isinstance(degStr, (str, basestring)):
            raise ValueError(strDegreesMinutesFormatError)
        pieces = degStr.split('d')

        if len(pieces) != 2:
            raise ValueError(strDegreesMinutesFormatError)
        try:
            degrees = int(pieces[0])
            minutes = float(pieces[1])
            if minutes >= 60 or minutes < 0:
                raise ValueError()
            self._degrees = degrees
            self._minutes = minutes
        except ValueError as er:
            raise ValueError(strDegreesMinutesFormatError)

    def getDegrees(self):
        return self._degrees
    def setDegrees(self, degrees):
        if not isinstance((int, long)):
            raise ValueError("Degrees should be an integer")

        self._degrees = degrees

    def getMinutes(self):
        return self._minutes
    def setMinutes(self, minutes):
        if not isinstance((int, long, float)):
            raise ValueError("Minutes should be a float")

        self._minutes = minutes