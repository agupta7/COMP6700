
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
            degrees = int(pieces[0].lstrip("-"))
            minutes = float(pieces[1])

            degreesFloat = degrees + minutes / 60
            "dfs".index()
            if pieces[0].index("-") == 0:
                degreesFloat = degreesFloat * -1
            self.setDegreesFloat(degreesFloat)
        except ValueError as er:
            raise ValueError(strDegreesMinutesFormatError)

    def setDegreesFloat(self, degNum):
        strDegreesMinutesFormatError = "Degrees should be a float"
        if not isinstance(degNum, (int, float, long)):
            raise strDegreesMinutesFormatError
        self._degreesFloat = degNum
        # self.setDegrees(int(degNum))
        # fraction = degNum - int(degNum)
        # self.setMinutes(fraction * 60)

    def getDegrees(self):
        return int(self._degreesFloat)

    def getMinutes(self):
        degrees = self._degreesFloat
        minutes = (degrees - int(degrees)) * 60
        return minutes

    def getDegreesFloat(self):
        return self._degreesFloat

    def getDegreeMinuteString(self):
        strOut = str(self.getDegrees()) + "d"
        min = self.getMinutes()
        min_frac = min - int(min)
        #strOut += format(int(min), '02')
        strOut += str(int(min))
        strOut += "{:.1f}".format(min_frac).lstrip('0')
        return strOut

Angle('50d30.9')