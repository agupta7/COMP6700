import pkg_resources
from softwareprocess.Angle import Angle
import datetime
import math

class NavigableStar:
    def __init__(self, starName):
        strStarInvalid = "Please specify a valid navigable star in string insensitive format."
        if not isinstance(starName, (str, basestring)):
            raise ValueError(strStarInvalid)

        config = self.getConfiguration()
        if not config.has_key(starName.lower()):
            raise ValueError(strStarInvalid)
        self._sha = Angle(config[starName.lower()].get('sha'))
        self._declination = Angle(config[starName.lower()].get('declination'))

    def predict(self, dateTime):
        observationDateTime = datetime.datetime.strptime(dateTime, "%Y-%m-%d %H:%M:%S")
        referencePoint = datetime.datetime.strptime("2001-01-1 00:00:00", "%Y-%m-%d %H:%M:%S")
        latlong = {'lat': self._declination.getDegreeMinuteString()}
        sha_star = self._sha

        gha_aries_referencepoint = Angle("100d42.6")

        years_diff = observationDateTime.year - referencePoint.year
        years_offset = Angle(Angle("0d14.31667").getDegreesFloat() * years_diff)

        leap_day_count =  self.getLeapDaysCount(observationDateTime)
        per_day_excess_rotation = Angle(360 - 86164.1/86400.0 * 360)
        leap_days_rotation = Angle(per_day_excess_rotation.getDegreesFloat() * leap_day_count)

        # step c in excel sheet : gha_aries_referencepoint + years_offset + leap_days_rotation

        begining_of_observation_year = datetime.datetime(observationDateTime.year, 1, 1)
        excess_time_diff = (observationDateTime - begining_of_observation_year)
        excess_seconds = excess_time_diff.days * 86400 + excess_time_diff.seconds
        excess_rotation = excess_seconds / 86164.1
        excess_rotation = excess_rotation - int(excess_rotation)
        excess_rotation = Angle(excess_rotation * 360)

        sum = gha_aries_referencepoint.getDegreesFloat() - years_offset.getDegreesFloat() + leap_days_rotation.getDegreesFloat() + excess_rotation.getDegreesFloat() + sha_star.getDegreesFloat()
        sum = sum % 360
        latlong['long'] = Angle(sum).getDegreeMinuteString()

        return latlong

    @classmethod
    def getLeapDaysCount(cls, dstDate):
        leapDays = 0
        numYears = dstDate.year - 2000
        leapDays += int(numYears / 4)

        if dstDate.year % 4 == 0:
            leapDays -= 1

        return leapDays

    @classmethod
    def getConfiguration(cls):
        cfgStr = cls._readConfiguration("starLocations.cfg")
        return cls._parseConfiguration(cfgStr)

    @classmethod
    def _readConfiguration(cls, resourceName):
        return pkg_resources.resource_string(__name__, resourceName)

    @classmethod
    def _parseConfiguration(cls, cfgStr):
        starDict = {}
        lines = cfgStr.split('\n')
        for line in lines:
                columns = line.split('\t')
                starName = columns[0]
                starDef = {'sha': columns[1], 'declination': columns[2]}
                starDict[starName.lower()] = starDef
        return starDict
