import pkg_resources
from softwareprocess.Angle import Angle
import datetime

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
        observationDateTime = datetime.datetime.strptime(dateTime, "%Y-%m")

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
