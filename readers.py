from helpers import normalizeDate


class Readers:
    def __init__(self, validator):
        self.validator = validator

    def readDates(self, d):
        self.validator.validateDates(d)
        return normalizeDate(d[0]), normalizeDate(d[1])

    def readMId(self, x):
        self.validator.validateMId(x)
        return int(x.strip())

    def readCId(self, x):
        self.validator.validateCId(x)
        return int(x.strip())

    def readRId(self, x):
        self.validator.validateRId(x)
        return int(x.strip())

    def readId(self, x):
        self.validator.validateId(x)
        return int(x.strip())

    def readName(self, s):
        return s.strip()

    def readCommand(self, s):
        s = s.strip()
        self.validator.validateCommand(s)
        return s

