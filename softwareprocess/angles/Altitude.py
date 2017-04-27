import softwareprocess.Angle as A

class Altitude(A.Angle):
    def setDegreesFloat(self, degNum):
        strAngleTooLowException = 'The altitude specified is too low!  It must be greater than 0 degrees and 0.0 minutes'
        strAltitudeTooHigh = 'The altitude specified is too high!  It must be less than 90 degrees and 0.0 minutes'
        if isinstance(degNum, (int, float, long)):
            if degNum <= 0:
                raise ValueError(strAngleTooLowException)
            elif degNum >= 90:
                raise ValueError(strAltitudeTooHigh)
        A.Angle.setDegreesFloat(self, degNum)
