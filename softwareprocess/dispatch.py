import softwareprocess.StarSighting as SS

def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        val = dispatchAdjust(values)
        return val
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values

def dispatchAdjust(values):
    if 'obervation' not in values:
        values['error'] = 'mandatory information is missing'
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