
from domain import Movie, Client, Rental
from helpers import isLeap, isDate, isDatePair, dateToDays, normalizeDate, isId
from validation import (
    validateDates, validateMId, validateCId,
    validateRId, validateId, validateCommand
)
from readers import readDates, readMId, readCId, readRId, readId, readName
from repository import (
    setMovies, setClients, setRentals,
    getMovieById, getClientById, getRentalById,
    getAllMovies, getAllClients, getAllRentals,
    movieExists, clientExists, rentalExists,
    addMovie, addClient, addRental,
    modifyMovie, modifyClient, modifyRental,
    deleteMovie, deleteClient, deleteRental,
    undoM, undoC, undoR
)
from command_process import process
from commands import getParams, getCommands, executeCommand
from ui import parse, readInput


# TEST SETUP

def resetRepository():
    setMovies({})
    setClients({})
    setRentals({})

    Movie.nextId = 1
    Client.nextId = 1
    Rental.nextId = 1


def loadTestData():
    resetRepository()

    addMovie("Shrek", "Adventure", "An ogre's adventure", 30)
    addMovie("Batman", "Action", "Gotham City", 15)

    addClient("John Smith", "1234567890123")
    addClient("Jane Smith", "2345678901234")

    addRental(1, 1, "01/11/2026", "10/11/2026")


# DOMAIN TESTS

def testDomain():
    resetRepository()

    movie = Movie("Shrek", "Adventure", "Ogre", 30)
    assert movie.getId() == 1
    assert movie.getTitle() == "Shrek"
    assert movie.getGenre() == "Adventure"
    assert movie.getDesc() == "Ogre"
    assert movie.getCopies() == 30

    movie.setTitle("Shrek 2")
    movie.setGenre("Comedy")
    movie.setDesc("Another adventure")
    movie.setCopies(20)

    assert movie.getTitle() == "Shrek 2"
    assert movie.getGenre() == "Comedy"
    assert movie.getDesc() == "Another adventure"
    assert movie.getCopies() == 20
    assert movie.getId() == 1

    client = Client("John", "1234567890123")
    assert client.getId() == 1
    assert client.getName() == "John"
    assert client.getCnp() == "1234567890123"

    client.setName("Jane")
    client.setCnp("2345678901234")

    assert client.getName() == "Jane"
    assert client.getCnp() == "2345678901234"
    assert client.getId() == 1

    rental = Rental(1, 1, "01/11/2026", "10/11/2026")
    assert rental.getId() == 1
    assert rental.getmId() == 1
    assert rental.getcId() == 1

    rental.setmId(2)
    rental.setcId(2)
    rental.setSdate("02/11/2026")
    rental.setDdate("12/11/2026")

    assert rental.getmId() == 2
    assert rental.getcId() == 2
    assert rental.getSdate() == "02/11/2026"
    assert rental.getDdate() == "12/11/2026"
    assert rental.getId() == 1


# HELPERS TESTS

def testHelpers():
    assert isLeap("01/01/2024")
    assert isLeap("01/01/2000")
    assert not isLeap("01/01/1900")
    assert not isLeap("01/01/2026")

    assert isDate("29/02/2024")
    assert not isDate("29/02/2026")
    assert not isDate("31/04/2026")
    assert not isDate("00/01/2026")
    assert not isDate("01/13/2026")
    assert not isDate("hello")

    assert dateToDays("02/01/2026") - dateToDays("01/01/2026") == 1
    assert dateToDays("01/03/2024") - dateToDays("28/02/2024") == 2
    assert dateToDays("01/01/2027") - dateToDays("31/12/2026") == 1

    assert isDatePair(("01/11/2026", "10/11/2026"))
    assert not isDatePair(("10/11/2026", "01/11/2026"))
    assert isDatePair(("01/11/2026", "01/11/2026"))

    assert normalizeDate(" 1 / 2 / 2026 ") == "1/2/2026"

    assert isId("123")
    assert isId(" 123 ")
    assert not isId("abc")
    assert not isId("12a")


# VALIDATION TESTS

def testValidation():
    loadTestData()

    assert validateMId("1")
    assert validateCId("1")
    assert validateRId("1")
    assert validateId("123")
    assert validateCommand("add movie")
    assert validateDates(("01/11/2026", "10/11/2026"))

    try:
        validateMId("999")
        assert False, "Nonexistent movie ID was accepted"
    except ValueError:
        pass

    try:
        validateCId("abc")
        assert False, "Invalid client ID was accepted"
    except ValueError:
        pass

    try:
        validateRId("999")
        assert False, "Nonexistent rental ID was accepted"
    except ValueError:
        pass

    try:
        validateId("hello")
        assert False, "Invalid numeric argument was accepted"
    except ValueError:
        pass

    try:
        validateCommand("fly movie")
        assert False, "Unknown command was accepted"
    except ValueError:
        pass

    try:
        validateDates(("20/11/2026", "10/11/2026"))
        assert False, "Reversed dates were accepted"
    except ValueError:
        pass

    try:
        validateDates(("29/02/2026", "10/03/2026"))
        assert False, "Impossible date was accepted"
    except ValueError:
        pass


# READER TESTS

def testReaders():
    loadTestData()

    assert readName("  Shrek  ") == "Shrek"
    assert readId(" 30 ") == 30
    assert readMId(" 1 ") == 1
    assert readCId(" 1 ") == 1
    assert readRId(" 1 ") == 1

    assert readDates(
        (" 01/11/2026 ", " 10/11/2026 ")
    ) == ("01/11/2026", "10/11/2026")

    try:
        readMId("999")
        assert False, "Invalid movie ID was accepted"
    except ValueError:
        pass

    try:
        readDates(("20/11/2026", "10/11/2026"))
        assert False, "Invalid date pair was accepted"
    except ValueError:
        pass


# MOVIE REPOSITORY TESTS

def testMovies():
    resetRepository()

    addMovie("Shrek", "Adventure", "Ogre", 30)
    assert getAllMovies() == [1]
    assert movieExists(1)
    assert getMovieById(1).getTitle() == "Shrek"

    addMovie("Batman", "Action", "Gotham", 15)
    assert getAllMovies() == [1, 2]

    modifyMovie(1, "Shrek 2", "Comedy", "Sequel", 20)

    movie = getMovieById(1)
    assert movie.getId() == 1
    assert movie.getTitle() == "Shrek 2"
    assert movie.getGenre() == "Comedy"
    assert movie.getDesc() == "Sequel"
    assert movie.getCopies() == 20

    undoM()
    assert getMovieById(1).getTitle() == "Shrek"
    assert getMovieById(1).getCopies() == 30

    deleteMovie(1)
    assert not movieExists(1)
    assert getMovieById(1) is None

    undoM()
    assert movieExists(1)
    assert getMovieById(1).getTitle() == "Shrek"

    try:
        deleteMovie(999)
        assert False, "Nonexistent movie was deleted"
    except ValueError:
        pass


# CLIENT REPOSITORY TESTS

def testClients():
    resetRepository()

    addClient("John", "1234567890123")
    assert getAllClients() == [1]
    assert clientExists(1)

    modifyClient(1, "Jane", "2345678901234")

    client = getClientById(1)
    assert client.getId() == 1
    assert client.getName() == "Jane"
    assert client.getCnp() == "2345678901234"

    undoC()
    assert getClientById(1).getName() == "John"

    deleteClient(1)
    assert not clientExists(1)

    undoC()
    assert clientExists(1)
    assert getClientById(1).getName() == "John"

    try:
        modifyClient(999, "Nobody", "123")
        assert False, "Nonexistent client was modified"
    except ValueError:
        pass


# RENTAL REPOSITORY TESTS

def testRentals():
    loadTestData()

    assert getAllRentals() == [1]
    assert rentalExists(1)

    rental = getRentalById(1)
    assert rental.getmId() == 1
    assert rental.getcId() == 1
    assert rental.getSdate() == "01/11/2026"
    assert rental.getDdate() == "10/11/2026"

    modifyRental(1, 2, 2, "05/11/2026", "15/11/2026")

    rental = getRentalById(1)
    assert rental.getId() == 1
    assert rental.getmId() == 2
    assert rental.getcId() == 2
    assert rental.getSdate() == "05/11/2026"
    assert rental.getDdate() == "15/11/2026"

    undoR()
    rental = getRentalById(1)
    assert rental.getmId() == 1
    assert rental.getcId() == 1
    assert rental.getSdate() == "01/11/2026"

    deleteRental(1)
    assert not rentalExists(1)

    undoR()
    assert rentalExists(1)

    try:
        deleteRental(999)
        assert False, "Nonexistent rental was deleted"
    except ValueError:
        pass


# EMPTY UNDO TESTS

def testEmptyUndo():
    resetRepository()

    for undo in (undoM, undoC, undoR):
        try:
            undo()
            assert False, "Empty undo history did not raise ValueError"
        except ValueError:
            pass


# COMMAND PARSING AND PROCESSING TESTS

def testCommands():
    loadTestData()

    parsed = parse("add movie; Shrek 2; Comedy; Sequel; 20")

    assert parsed[0] == "add movie"
    assert parsed[1] == ["Shrek 2", "Comedy", "Sequel", "20"]

    assert getParams("add movie") == (4, "NNNI")
    assert getParams("add rental") == (4, "mcP")
    assert "delete movie" in getCommands()

    result = process((
        "add movie",
        ["Shrek 2", "Comedy", "Sequel", "20"]
    ))

    assert result == ["Shrek 2", "Comedy", "Sequel", 20]

    result = process((
        "add rental",
        ["1", "1", "01/11/2026", "10/11/2026"]
    ))

    assert result == [1, 1, "01/11/2026", "10/11/2026"]

    assert process(("help", [])) == []

    try:
        process(("add movie", ["Shrek", "Adventure"]))
        assert False, "Incorrect argument count was accepted"
    except ValueError:
        pass

    try:
        process((
            "add rental",
            ["1", "1", "20/11/2026", "10/11/2026"]
        ))
        assert False, "Invalid rental dates were accepted"
    except ValueError:
        pass


# END-TO-END COMMAND TESTS

def testCommandExecution():
    resetRepository()

    command, args = readInput(
        "add movie; Shrek; Adventure; Ogre; 30"
    )
    executeCommand(command, args)

    assert movieExists(1)
    assert getMovieById(1).getCopies() == 30

    command, args = readInput(
        "edit movie; 1; Shrek 2; Comedy; Sequel; 20"
    )
    executeCommand(command, args)

    assert getMovieById(1).getTitle() == "Shrek 2"
    assert getMovieById(1).getCopies() == 20

    command, args = readInput("undoM")
    executeCommand(command, args)

    assert getMovieById(1).getTitle() == "Shrek"

    command, args = readInput(
        "add client; John Smith; 1234567890123"
    )
    executeCommand(command, args)

    assert clientExists(1)

    command, args = readInput(
        "add rental; 1; 1; 01/11/2026; 10/11/2026"
    )
    executeCommand(command, args)

    assert rentalExists(1)

    try:
        readInput(
            "add rental; 1; 1; 20/11/2026; 10/11/2026"
        )
        assert False, "Invalid rental command was accepted"
    except ValueError:
        pass

    try:
        readInput("unknown command")
        assert False, "Unknown command was accepted"
    except ValueError:
        pass


# RUN ALL TESTS

def runAllTests():
    tests = [
        testDomain,
        testHelpers,
        testValidation,
        testReaders,
        testMovies,
        testClients,
        testRentals,
        testEmptyUndo,
        testCommands,
        testCommandExecution
    ]

    passed = 0

    try:
        for test in tests:
            test()
            print(f"[PASS] {test.__name__}")
            passed += 1
    finally:
        resetRepository()

    print(f"\nAll {passed} test groups passed!")


if __name__ == "__main__":
    runAllTests()
