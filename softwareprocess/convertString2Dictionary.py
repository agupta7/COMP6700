import urllib
import re

def convertString2Dictionary(inputString = ""):
    errorDict = {'error':'true'}
    outDict = dict()
    parseMe = urllib.unquote(inputString)

    # check the error cases and fail fast
    if parseMe == "":
        return errorDict

    # basic regex test to see if the string contains invalid characters at all
    matches = re.match("^[A-Za-z0-9 \.,=]*$", parseMe) # basic sanity check to see if the string has any invalid characters
    if matches is None:
        return errorDict
    keyPattern = re.compile("^[A-Za-z][A-Za-z0-9\.]*$") # key must start with a letter and be followed by alphanumeric and/or '.' characters
    valuePattern = re.compile("^[A-Za-z0-9\.]+$") # value can be any combination of alphanumeric and/or '.' characters with a length of at least 1

    pieces = parseMe.split(",")
    for piece in pieces:
        keyValuePair = piece.split("=")
        if len(keyValuePair) != 2: # must have one and exactly one equal sign
            return errorDict
        key = keyValuePair[0].strip()
        if keyPattern.match(key) is None:
            return errorDict
        if key in outDict: # duplicate key error
            return errorDict
        value = keyValuePair[1].strip()
        if valuePattern.match(value) is None:
            return errorDict
        outDict[key] = value

    return outDict