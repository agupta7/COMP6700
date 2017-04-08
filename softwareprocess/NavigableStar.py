import pkg_resources

class NavigableStar:
    def __init__(self, starName):
        strStarInvalid = "Please specify a valid navigable star in string insensitive format."
        if not isinstance(starName, (str, basestring)):
            raise strStarInvalid

        config = self.getConfiguration()
        if not config.has_key(starName.lower()):
            raise strStarInvalid
        self._sha = config[starName.lower()].get('sha')
        self._declination = config[starName.lower()].get('declination')

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
            starDef = {}
            starDef['sha'] = columns[1]
            starDef['declination'] = columns[2]
            starDict[starName.lower()] = starDef
        return starDict
