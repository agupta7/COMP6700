import softwareprocess.angles.Latitude as Lat
import softwareprocess.angles.Altitude as Alt
import softwareprocess.angles.Longitude as Long

class SightingErrorCorrector:
    def __init__(self, lat, long, altitude, assumedLat, assumedLong):
        self._lat = Lat.Latitude(lat)
        self._long = Long.Longitude(long)
        self._altitude = Alt.Altitude(altitude)
        self._assumedLat = Lat.Latitude(assumedLat)
        self._assumedLong = Long.Longitude(assumedLong)