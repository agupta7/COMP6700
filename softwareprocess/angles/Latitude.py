import softwareprocess.Angle as A

class Latitude(A.Angle):
    def setDegreesFloat(self, degNum):
        latitudeTooLowStr = 'The latitude specified is too low!  It must be greater than -90 degrees and 0.0 minutes'
        latitudeTooHighStr = 'The latitude specified is too high!  It must be less than 90 degrees and 0.0 minutes'
        if isinstance(degNum, (int, float, long)):
            if degNum <= -90:
                raise ValueError(latitudeTooLowStr)
            elif degNum >= 90:
                raise ValueError(latitudeTooHighStr)
        A.Angle.setDegreesFloat(self, degNum)