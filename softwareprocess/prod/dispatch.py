import softwareprocess.StarSighting as SS
from softwareprocess.NavigableStar import NavigableStar
from softwareprocess.Angle import Angle
import softwareprocess.SightingErrorCorrector as SEC

def dispatch(values=None):
    def dispatchAdjust(values):
        if 'observation' not in values:
            values['error'] = 'mandatory information is missing'
            return values
        if 'altitude' in values:
            values['error'] = 'altitude should not be present in input'
            return values

        try:
            ss = SS.StarSighting.fromDegreeMinString(values['observation'])
        except Exception:
            values['error'] = 'observation is invalid'
            return values

        if 'height' in values:
            try:
                ss.setHeight(float(values['height']))
            except Exception:
                values['error'] = 'height is invalid'
                return values

        if 'temperature' in values:
            try:
                ss.setTemperature(int(values['temperature']))
            except Exception:
                values['error'] = 'temperature is invalid'
                return values

        if 'pressure' in values:
            try:
                ss.setPressure(int(values['pressure']))
            except Exception:
                values['error'] = 'pressure is invalid'
                return values

        if 'horizon' in values:
            try:
                ss.setHorizon(values['horizon'])
            except Exception:
                values['error'] = 'horizon is invalid'
                return values

        values['altitude'] = ss.getAltitude()
        return values

    def dispatchPredict(values):
        if 'body' not in values:
            values['error'] = 'The name of the star is mandatory as the key body'
            return values
        if 'lat' in values or 'long' in values:
            values['error'] = "The keys 'lat' or 'long' should not be present in the input."
            return values

        if not isinstance(values['body'], (str, basestring)):
            values['error'] = "The value for the key 'body' should be a string."
            return values
        if 'date' in values and not isinstance(values['date'], (str, basestring)):
            values['error'] = "The value for the key 'date' should be a string."
            return values
        if 'time' in values and not isinstance(values['time'], (str, basestring)):
            values['error'] = "The value for the key 'time' should be a string."
            return values

        try:
            star = NavigableStar(values['body'])
        except:
            values['error'] = "Please specify a valid navigable star in string insensitive format in the key 'body'."
            return values

        dateTimeStr = "2001-01-01"
        if 'date' in values:
            dateTimeStr = values['date']

        if 'time' in values:
            dateTimeStr += " " + values['time']
        else:
            dateTimeStr += " 00:00:00"
        try:
            latlong = star.predict(dateTimeStr)
        except:
            values['error'] = "The key 'date' should be in the format yyyy-mm-dd and the key 'time' should be in the 24-hr format HH:MM:SS."
            return values
        values['lat'] = latlong.get("lat")
        values['long'] = latlong.get("long")

        return values

    def dispatchCorrect(values):
        if not (isinstance(values.get('lat'), basestring) and isinstance(values.get('long'), basestring) and
                    isinstance(values.get('altitude'), basestring) and isinstance(values.get('assumedLat'), basestring) and
                    isinstance(values.get('assumedLong'), basestring)):
            values['error'] = "All parameters (lat, long, altitude, assumedLat, assumedLong) must be passed and be strings."
            return values

        if 'correctedAzimuth' in values:
            values['error'] = "correctedAzimuth can't be present in the input parameter list."
            return values
        elif 'correctedDistance' in values:
            values['error'] = "correctedDistance can't be present in the input parameter list."
            return values
        try:
            sec = SEC.SightingErrorCorrector(values['lat'], values['long'], values['altitude'], values['assumedLat'], values['assumedLong'])
            correction = sec.correct()
        except Exception as e:
            values['error'] = str(e.args[0])
            return values

        values['correctedAzimuth'] = correction['correctedAzimuth']
        values['correctedDistance'] = correction['correctedDistance']
        return values
    # Validate parm
    if (values == None):
        return {'error': 'parameter is missing'}
    if (not (isinstance(values, dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not ('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    # Perform designated function
    if (values['op'] == 'adjust'):
        val = dispatchAdjust(values)
        return val
    elif (values['op'] == 'predict'):
        val = dispatchPredict(values)
        return val
    elif (values['op'] == 'correct'):
        return dispatchCorrect(values)
    elif (values['op'] == 'locate'):
        return values  # This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values