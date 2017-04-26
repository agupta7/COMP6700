import softwareprocess.Angle as A

class Longitude(A.Angle):
    def __init__(self, degreesStrOrFloat):
        longitudeTooLowStr = 'The longitude specified is too low!  It must be greater than or equal to 0 degrees and 0.0 minutes'
        longitudeTooHighStr = 'The longitude specified is too high!  It must be less than 360 degrees and 0.0 minutes'
        A.Angle.__init__(self, degreesStrOrFloat)
        if self._degreesFloat < 0:
            raise ValueError(longitudeTooLowStr)
        elif self._degreesFloat >= 360:
            raise ValueError(longitudeTooHighStr)