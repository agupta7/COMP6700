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
        self._temperatureF = 72
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
    def setTemperature(self, temperature):
        strTemperatureError = "Temperature should be an integer >= -20 & <= 120 in Farenheit"
        if not isinstance(temperature, (int, long)) or temperature < -20 or temperature > 120:
            raise ValueError(strTemperatureError)

        self._temperatureF = temperature
        return self
    def getTemperature(self):
        return self._temperatureF
    def getTemperatureKelvin(self):
        return 273 + (self._temperatureF - 32) * 5/9

    def setPressure(self, pressure):
        strPressureError = "Pressure should be an integer >= 100 & <= 1100 in millibars"
        if not isinstance(pressure, (int, long)) or pressure < 100 or pressure > 1100:
            raise ValueError(strPressureError)

        self._pressureMillibar = pressure
        return self
    def getPressure(self):
        return self._pressureMillibar

    def setHorizon(self, horizon):
        strHorizonError = "Horizon should be 'artificial' or 'natural'"
        if not isinstance(horizon, (str, basestring)) or (horizon.lower() != 'natural' and horizon.lower() != 'artificial'):
            raise ValueError(strHorizonError)

        if horizon.lower() == 'natural':
            self._horizonNaturalArtificial = 0
        else:
            self._horizonNaturalArtificial = 1

        return self

    def getHorizon(self):
        if self._horizonNaturalArtificial == 0:
            return 'natural'
        else:
            return 'artificial'

    @classmethod
    def fromDegreeMinString(cls, degStr):
        strDegreesMinutesFormatError = "String should in format XdY.Y where X is degrees and Y.Y is floating point minutes"

        if not isinstance(degStr, (str, basestring)):
            raise ValueError(strDegreesMinutesFormatError)
        pieces = degStr.split('d')

        if len(pieces) != 2:
            raise ValueError(strDegreesMinutesFormatError)
        try:
            degrees = int(pieces[0])
            minutes = float(pieces[1])
        except ValueError as er:
            raise ValueError(strDegreesMinutesFormatError)

        return StarSighting(degrees, minutes)

    def getAngle(self):
        return self.getDegrees() + self.getMinutes() / 60

    def getAltitude(self):
        altitude = float(self._calculateAltitude())
        formatted = str(int(altitude)) + 'd'
        minutes = (altitude % 1) * 60
        formatted += str(round(minutes, 1))

    def _calculateAltitude(self):
        dip = 0
        if self._horizonNaturalArtificial == 0:
            dip = -0.97 * math.sqrt(self.getHeight()) / 60

        deg = self.getDegrees() + self.getMinutes() / 60
        refraction = -0.00452 * self.getPressure() / self.getTemperatureKelvin() / math.tan(deg * math.pi / 180)
        altitude = deg + dip + refraction
        return altitude