from helpers import isDate, isId, isDatePair


class Validator():
    def __init__(self, repos):
        self.commands = []
        self.repos = repos

    def setCommandNames(self, names):
        self.commands = names

    def validateDates(self, d):
        if isDate(d[0]) and isDate(d[1]):
            if isDatePair(d):
                return True

        raise ValueError("Dates must be in the format dd/mm/yyyy and start date must be before due date!")

    def validateMId(self, x):
        if isId(x):
            if int(x.strip()) in self.repos.getAllMovies():
                return True

    def validateCId(self, x):
        if isId(x):
            if int(x.strip()) in self.repos.getAllClients():
                return True

    def validateRId(self, x):
        if isId(x):
            if int(x.strip()) in self.repos.getAllRentals():
                return True

        raise ValueError("Rental ID does not exist or is not an integer!")

    def validateId(self, x):
        # for generic ID-like arguments like copies or CNP
        if isId(x):
            return True
        else:
            raise ValueError("Copies, CNPs must be numbers!")

    def validateCommand(self, s):
        if s in self.commands:
            return True
        else:
            raise ValueError("Invalid command! Type [help] for a list of all commands")















