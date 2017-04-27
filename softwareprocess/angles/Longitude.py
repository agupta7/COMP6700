import softwareprocess.Angle as A

class Longitude(A.Angle):
    def setDegreesFloat(self, degNum):
        longitudeTooLowStr = 'The longitude specified is too low!  It must be greater than or equal to 0 degrees and 0.0 minutes'
        longitudeTooHighStr = 'The longitude specified is too high!  It must be less than 360 degrees and 0.0 minutes'
        if isinstance(degNum, (int, float, long)):
            if degNum < 0:
                raise ValueError(longitudeTooLowStr)
            elif degNum >= 360:
                raise ValueError(longitudeTooHighStr)
        A.Angle.setDegreesFloat(self, degNum)