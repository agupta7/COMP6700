import softwareprocess.Angle as A

class Altitude(A.Angle):
    def __init__(self, degreesStrOrFloat):
        strAngleTooLowException = 'The altitude specified is too low!  It must be greater than 0 degrees and 0.0 minutes'
        A.Angle.__init__(self, degreesStrOrFloat)
        if self._degreesFloat <= 0:
            raise ValueError(strAngleTooLowException)
