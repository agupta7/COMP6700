import softwareprocess.Angle as A

class Latitude(A.Angle):
    def __init__(self, degreesStrOrFloat):
        latitudeTooLowStr = 'The latitude specified is too low!  It must be greater than -90 degrees and 0.0 minutes'
        latitudeTooHighStr = 'The latitude specified is too high!  It must be less than 90 degrees and 0.0 minutes'
        A.Angle.__init__(self, degreesStrOrFloat)
        if self._degreesFloat <= -90:
            raise ValueError(latitudeTooLowStr)
        elif self._degreesFloat >= 90:
            raise ValueError(latitudeTooHighStr)