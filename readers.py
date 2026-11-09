from helpers import normalizeDate
from validation import validateDates, validateMId, validateCId, validateRId, validateId, validateCommand


def readDates(d):
    #d has been already read. here it calls validation and returns the date properly formatted
    #d is also a tuple of a start and an end date, start must be before end
    validateDates(d)
    return normalizeDate(d[0]), normalizeDate(d[1])

def readMId(x):
    validateMId(x)
    return int(x.strip())

def readCId(x):
    validateCId(x)
    return int(x.strip())

def readRId(x):
    validateRId(x)
    return int(x.strip())

def readId(x):
    #for generic ID-like arguments like copies or CNP (reused isId() from helpers, thus the name)
    validateId(x)
    return int(x.strip())

def readName(s):
    return s.strip()

def readCommand(s):
    validateCommand(s)
    return s.strip()