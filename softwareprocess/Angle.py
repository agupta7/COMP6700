
class Angle:
    def __init__(self, angle):
        if isinstance(angle, (str, basestring)):
            self.setDegreesString(angle)
        elif isinstance(angle, (int, long, float)):
            self.setDegreesFloat(float(angle))
        else:
            raise ValueError("String should in format XdY.Y where X is degrees and Y.Y is floating point minutes")

    def setDegreesString(self, degStr):
        strDegreesMinutesFormatError = "String should in format XdY.Y where X is degrees and Y.Y is floating point minutes"
        if not isinstance(degStr, (str, basestring)) :
            raise ValueError(strDegreesMinutesFormatError)
        pieces = degStr.split('d')

        if len(pieces) != 2:
            raise ValueError(strDegreesMinutesFormatError)
        try:
            if pieces[1].index('.') < 0:
                raise ValueError()
            degrees = int(pieces[0])
            minutes = float(pieces[1])

            self.setDegrees(degrees)
            self.setMinutes(minutes)
        except ValueError as er:
            raise ValueError(strDegreesMinutesFormatError)

    def setDegreesFloat(self, degNum):
        strDegreesMinutesFormatError = "Degrees should be a float"
        if not isinstance(degNum, (int, float, long)):
            raise strDegreesMinutesFormatError
        self.setDegrees(int(degNum))
        fraction = degNum - int(degNum)
        self.setMinutes(fraction * 60)

    def getDegrees(self):
        return self._degrees
    def setDegrees(self, degrees):
        if not isinstance(degrees, (int, long)):
            raise ValueError("Degrees should be an integer")

        self._degrees = degrees

    def getMinutes(self):
        return self._minutes
    def setMinutes(self, minutes):
        if not isinstance(minutes, (int, long, float)):
            raise ValueError("Minutes should be a float")
        if minutes >= 60 or minutes < 0:
            raise ValueError("Minutes can not be 60 or more or less than 0")
        self._minutes = minutes

    def getOnlyDegrees(self):
        return self.getDegrees() + self.getMinutes() / 60

    def getDegreeMinuteString(self):
        strOut = str(self.getDegrees()) + "d"
        min = self.getMintues()
        min_frac = int(min) - min
        strOut += format(int(min), '02')
        strOut += "{:.1f}".format(min_frac).lstrip('0')
