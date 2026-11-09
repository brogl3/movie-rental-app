from helpers import isDate, isId, isDatePair
from repository import getAllMovies, getAllClients, getAllRentals
from commands import getCommands


def validateDates(d):
    if isDate(d[0]) and isDate(d[1]):
        if isDatePair(d):
            return True

    raise ValueError("Dates must be in the format dd/mm/yyyy and start date must be before due date!")

def validateMId(x):
    if isId(x):
        if int(x.strip()) in getAllMovies():
            return True

    raise ValueError("Movie ID does not exist or is not an integer!")

def validateCId(x):
    if isId(x):
        if int(x.strip()) in getAllClients():
            return True

    raise ValueError("Client ID does not exist or is not an integer!")

def validateRId(x):
    if isId(x):
        if int(x.strip()) in getAllRentals():
            return True

    raise ValueError("Rental ID does not exist or is not an integer!")

def validateId(x):
    #for generic ID-like arguments like copies or CNP
    if isId(x):
        return True
    else:
        raise ValueError("Copies, CNPs must be numbers!")

def validateCommand(s):
    if s in getCommands():
        return True
    else:
        raise ValueError("Invalid command! Type [help] for a list of all commands")





