import math

class Angle:
    def __init__(self, angle):
        if isinstance(angle, (str, basestring)):
            self.setDegreesString(angle)
        elif isinstance(angle, (int, long, float)):
            self.setDegreesFloat(float(angle))
        elif isinstance(angle, Angle):
            self.setDegreesFloat(angle._degreesFloat)
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
            if pieces[1].find('.') < 0:
                raise ValueError()
            degrees = int(pieces[0].lstrip("-"))
            minutes = float(pieces[1])
            if minutes >= 60 or minutes < 0:
                raise ValueError()

            degreesFloat = degrees + minutes / 60
            if pieces[0].find("-") == 0:
                degreesFloat = degreesFloat * -1
        except ValueError as er:
            raise ValueError(strDegreesMinutesFormatError)
        self.setDegreesFloat(degreesFloat)

    def setDegreesFloat(self, degNum):
        strDegreesMinutesFormatError = "Degrees should be a float"
        if not isinstance(degNum, (int, float, long)):
            raise strDegreesMinutesFormatError
        self._degreesFloat = degNum

    def getDegreesFloat(self):
        return self._degreesFloat

    def getRadiansFloat(self):
        return math.pi / 180 * self.getDegreesFloat()

    def getDegreeMinuteString(self):
        minutesTotal = round(self._degreesFloat * 60, 1)
        degrees = int(minutesTotal / 60)
        strOut = str(abs(degrees)) + "d"
        if minutesTotal < 0:
            strOut = "-" + strOut
        min = abs(minutesTotal - degrees * 60)
        min_frac = min - int(min)
        #strOut += format(int(min), '02')
        strOut += str(float(min))
        #strOut += "{:.1f}".format(min_frac).lstrip('0')
        return strOut
