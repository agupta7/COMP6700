import softwareprocess.angles.Latitude as Lat
import softwareprocess.angles.Altitude as Alt
import softwareprocess.angles.Longitude as Long
import softwareprocess.Angle as Ang
import math

class SightingErrorCorrector:
    def __init__(self, lat, long, altitude, assumedLat, assumedLong):
        self._lat = Lat.Latitude(lat)
        self._long = Long.Longitude(long)
        self._altitude = Alt.Altitude(altitude)
        self._assumedLat = Lat.Latitude(assumedLat)
        self._assumedLong = Long.Longitude(assumedLong)

    def correct(self):
        latRad = self._lat.getRadiansFloat()
        longRad = self._long.getRadiansFloat()
        altRad = self._altitude.getRadiansFloat()
        assLatRad = self._assumedLat.getRadiansFloat()
        assLongRad = self._assumedLong.getRadiansFloat()

        # step A : calculate the local hour angle of the navigator
        LHA = Ang.Angle(self._long.getDegreesFloat() + self._assumedLong.getDegreesFloat())

        # step B : calculate the angle by which to adjust the observed altitude to match the star observed from the assumed position
        intermediateDistance = math.sin(latRad) * math.sin(assLatRad) + \
            math.cos(latRad) * math.cos(assLatRad) * math.cos(LHA.getRadiansFloat())
        correctedAltitude = math.asin(intermediateDistance)
        correctedAltitude = Ang.Angle(correctedAltitude / math.pi * 180.0)

        # step C : Calculate distance the navigator needs to move.  Convert to arc-minutes and round to nearest 0.1
        correctedDistance = self._altitude.getDegreesFloat() - correctedAltitude.getDegreesFloat() # distance in fractional degrees
        correctedDistanceArcMinutes = round(correctedDistance * 60, 1)

        # step D : Determine the compass direction in which to make the distance adjustment:
        correctedAzimuth = math.acos(\
                ( math.sin(latRad) - math.sin(assLatRad) * intermediateDistance   ) /
                ( math.cos(assLatRad) * math.cos(math.asin(intermediateDistance)) )
            )
        correctedAzimuth = Ang.Angle(correctedAzimuth / math.pi * 180.0)

        return {'correctedDistance': str(correctedDistanceArcMinutes), 'correctedAzimuth': correctedAzimuth.getDegreeMinuteString()}

