import softwareprocess.SightingErrorCorrector as SEC
import unittest

class SightingErrorCorrectorTest(unittest.TestCase):

# ---------  Acceptance tests------------
#---- 100 constructor
#------- input :    lat         - 'XdY.Y' format like elsewhere.  -90 < lat < 90
#------             long        - 'XdY.Y' format like elsewhere.  0<= long < 360
#-------            altitude    - 'XdY.Y' format like elsewhere.  0 < alt < 90
#-------            assumedLat  - 'XdY.Y' format like elsewhere.  -90 < lat < 90
#-------            assumedLong - 'XdY.Y' format like elsewhere.  0 <= lat < 360
#------  output   : instance of SightingErrorCorrector
#--------- Happy path analysis
# ----   input : nominal inputs ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ----   input : high inputs ('89d59.9' lat, '359d59.9' long, '89d59.9' altitude, '89d59.9' assumedLat, '359d59.9' assumedLong)
# ----  input : low inputs ('-89d59.9' lat, '0d0.0' long, '0d0.1' altitude, '-89d59.9' assumedLat, '0d0.0' assumedLong)
# ---------Sad path analysis
#-------- input : one of the arguments is too high
#------------------lat too high ('90d0.0' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ------------------long too high ('16d32.3' lat, '360d0.0' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ------------------altitude too high ('16d32.3' lat, '95d41.6' long, '90d0.0' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
# ------------------assumedLat too high ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '90d0.0' assumedLat, '74d35.3' assumedLong)
# ------------------assumedLong too high ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '360d0.0' assumedLong)
#--------output : ValueError raised explaining which value was too high
#------- input : one of the parameters is too low
#-----------------lat is too low ('-90d0.0' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#-----------------long is too low ('16d32.3' lat, '-0d0.1' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#-----------------altitude is too low ('16d32.3' lat, '95d41.6' long, '0d0.0' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#-----------------assumedLat is too low ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-90d0.0' assumedLat, '74d35.3' assumedLong)
#-----------------assumedLong is too low ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '-0d0.1' assumedLong)
#------ output : ValueError raised explaining which value was too low

    def test100_010_ShouldConstructNominalInputs(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(sec, SEC.SightingErrorCorrector)
    def test100_020_ShouldConstructHighInputs(self):
        lat = '89d59.9'
        long = '359d59.9'
        alt = '89d59.9'
        assumedLat = '89d59.9'
        assumedLong = '359d59.9'

        sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(sec, SEC.SightingErrorCorrector)
    def test100_030_ShouldConstructLowInputs(self):
        lat = '-89d59.9'
        long = '0d0.0'
        alt = '0d0.1'
        assumedLat = '-89d59.9'
        assumedLong = '0d0.0'

        sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(sec, SEC.SightingErrorCorrector)

    def test100_810_ShouldRaiseValueErrorLatTooHigh(self):
        lat = '90d0.0'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_820_ShouldRaiseValueErrorLongTooHigh(self):
        lat = '16d32.3'
        long = '360d0.0'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_830_ShouldRaiseValueErrorAltitudeTooHigh(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '90d0.0'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_840_ShouldRaiseValueErrorAssumedLatTooHigh(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '90d0.0'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_850_ShouldRaiseValueErrorAssumedLongTooHigh(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '360d0.0'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))

    def test100_910_ShouldRaiseValueErrorLatTooLow(self):
        lat = '-90d0.0'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_920_ShouldRaiseValueErrorLongTooLow(self):
        lat = '16d32.3'
        long = '-0d0.1'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_930_ShouldRaiseValueErrorAltitudeTooLow(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '0d0.0'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_940_ShouldRaiseValueErrorAssumedLatTooLow(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-90d0.0'
        assumedLong = '74d35.3'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))
    def test100_950_ShouldRaiseValueErrorAssumedLongTooLow(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '-0d0.1'

        with self.assertRaises(ValueError) as ctx:
            sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        self.assertIsInstance(ctx.exception.args[0], (str, basestring))

#---- 200 correct
#---- Happy path analysis
#----   input nominal values : ('16d32.3' lat, '95d41.6' long, '13d42.3' altitude, '-53d38.4' assumedLat, '74d35.3' assumedLong)
#----   output : {'correctedDistance' : '3950', 'correctdAzimuth' : '164d42.9'}
#----   input values : ('89d20.1' lat, '154d5.4' long, '37d17.4' altitude, '35d59.7' assumedLat, '74d35.3' assumedLong)
#----   output : {'correctedDistance': '104', 'correctedAzimuth': '0d36.8'}
#---- Sad path analysis is none because it works on validated instance variables

    def test200_010ShouldCalculateCorrectionExample2(self):
        lat = '16d32.3'
        long = '95d41.6'
        alt = '13d42.3'
        assumedLat = '-53d38.4'
        assumedLong = '74d35.3'

        sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        correction = sec.correct()
        self.assertAlmostEquals(float(correction.get('correctedDistance')), 3950, delta=0.15)
        self.assertEquals(correction.get('correctedAzimuth'), '164d42.9')
    def test200_020ShouldCalculateCorrectionExample1(self):
        lat = '89d20.1'
        long = '154d5.4'
        alt = '37d17.4'
        assumedLat = '35d59.7'
        assumedLong = '74d35.3'

        sec = SEC.SightingErrorCorrector(lat=lat, long=long, altitude=alt, assumedLat=assumedLat, assumedLong=assumedLong)
        correction = sec.correct()
        self.assertAlmostEquals(float(correction.get('correctedDistance')), 104, delta=0.15)
        self.assertEquals(correction.get('correctedAzimuth'), '0d36.8')