from helpers import isDate, isId, isDatePair


class Validator:
    def __init__(self, repositories):
        self.repos = repositories
        self.commandNames = []

    def setCommandNames(self, names):
        self.commandNames = names

    def validateDates(self, d):
        if isDate(d[0]) and isDate(d[1]):
            if isDatePair(d):
                return True
        raise ValueError("Dates must be in the format dd/mm/yyyy and start date must be before due date!")

    def validateMId(self, x):
        if isId(x):
            if self.repos.movies.movieExists(int(x.strip())):
                return True
        raise ValueError("Movie ID does not exist or is not an integer!")

    def validateCId(self, x):
        if isId(x):
            if self.repos.clients.clientExists(int(x.strip())):
                return True
        raise ValueError("Client ID does not exist or is not an integer!")

    def validateRId(self, x):
        if isId(x):
            if self.repos.rentals.rentalExists(int(x.strip())):
                return True
        raise ValueError("Rental ID does not exist or is not an integer!")

    def validateId(self, x):
        if isId(x):
            return True
        else:
            raise ValueError("Copies, CNPs must be numbers!")

    def validateCommand(self, s):
        if s in self.commandNames:
            return True
        else:
            raise ValueError("Invalid command! Type [help] for a list of all commands")
