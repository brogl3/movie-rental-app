from repository_movies import Movies
from repository_clients import Clients
from repository_rentals import Rentals


class RepositoryManager:
    def __init__(self):
        self.movies = Movies()
        self.clients = Clients()
        self.rentals = Rentals()

    def initializeRepository(self):
        self.movies.setMovies({})
        self.clients.setClients({})
        self.rentals.setRentals({})

        # MOVIES
        self.movies.addMovie("Shrek", "Animation", "An ogre's adventure", 12)
        self.movies.addMovie("The Dark Knight", "Action", "Batman faces the Joker", 8)
        self.movies.addMovie("Interstellar", "Sci-Fi", "A journey through space", 15)
        self.movies.addMovie("The Godfather", "Crime", "The Corleone family", 6)
        self.movies.addMovie("Inception", "Sci-Fi", "Dreams within dreams", 10)
        self.movies.addMovie("Titanic", "Romance", "A love story aboard the Titanic", 7)
        self.movies.addMovie("The Matrix", "Sci-Fi", "A hacker discovers reality", 11)
        self.movies.addMovie("Gladiator", "Action", "A Roman general seeks revenge", 9)
        self.movies.addMovie("Pulp Fiction", "Crime", "Interconnected criminal stories", 5)
        self.movies.addMovie("Finding Nemo", "Animation", "A father's ocean adventure", 14)

        # CLIENTS
        self.clients.addClient("John", "5010101123456")
        self.clients.addClient("Jane", "6020212123456")
        self.clients.addClient("Jeremy", "5030313123456")
        self.clients.addClient("Joelle", "6040414123456")
        self.clients.addClient("Jeff", "5050515123456")
        self.clients.addClient("Joana", "6060616123456")

        # RENTALS
        self.rentals.addRental(1, 1, "01/11/2026", "10/11/2026")
        self.rentals.addRental(3, 2, "03/11/2026", "12/11/2026")
        self.rentals.addRental(5, 3, "04/11/2026", "14/11/2026")
        self.rentals.addRental(2, 4, "05/11/2026", "15/11/2026")
        self.rentals.addRental(7, 5, "06/11/2026", "16/11/2026")
        self.rentals.addRental(10, 6, "07/11/2026", "17/11/2026")

        # Sample data should not count as user actions
        self.movies._history.clear()
        self.clients._history.clear()
        self.rentals._history.clear()
"""
movies = {}
clients = {}
rentals = {}

mhistory = []
chistory = []
rhistory = []


# HISTORY MANAGEMENT

def cloneDict(d):
    return deepcopy(d)


def saveMovies():
    mhistory.append(cloneDict(movies))


def saveClients():
    chistory.append(cloneDict(clients))


def saveRentals():
    rhistory.append(cloneDict(rentals))




def createMovie(title, genre, desc, copies):
    return Movie(title, genre, desc, copies)


def createClient(name, cnp):
    return Client(name, cnp)


def createRental(mid, cid, sdate, ddate):
    return Rental(mid, cid, sdate, ddate)




def getMovieById(id):
    return movies.get(id)


def getClientById(id):
    return clients.get(id)


def getRentalById(id):
    return rentals.get(id)


def getAllMovies():
    return [movie.getId() for movie in movies.values()]


def getAllClients():
    return [client.getId() for client in clients.values()]


def getAllRentals():
    return [rental.getId() for rental in rentals.values()]


# EXISTENCE CHECKS

def clientExists(id):
    return id in clients


def movieExists(id):
    return id in movies


def rentalExists(id):
    return id in rentals


# ADD OPERATIONS

def addMovie(title, genre, desc, copies):
    saveMovies()
    movie = createMovie(title, genre, desc, copies)
    movies[movie.getId()] = movie


def addClient(name, cnp):
    saveClients()
    client = createClient(name, cnp)
    clients[client.getId()] = client


def addRental(mid, cid, sdate, ddate):
    saveRentals()
    rental = createRental(mid, cid, sdate, ddate)
    rentals[rental.getId()] = rental


# DELETE OPERATIONS

def deleteMovie(id):
    if id not in movies:
        raise ValueError("Movie ID does not exist!")

    saveMovies()
    saveRentals()

    ok = 0
    for rid in list(rentals):
        if rentals[rid].getmId() == id:
            del rentals[rid]
            ok = 1

    del movies[id]
    if ok == 0:
        undoR()

def deleteClient(id):
    if id not in clients:
        raise ValueError("Client ID does not exist!")

    saveClients()
    saveRentals()
    ok = 0
    for rid in list(rentals):
        if rentals[rid].getcId() == id:
            del rentals[rid]
            ok = 1

    del clients[id]
    if ok == 0:
        undoR()

def deleteRental(id):
    if id not in rentals:
        raise ValueError("Rental ID does not exist!")

    saveRentals()
    del rentals[id]


# MODIFY OPERATIONS

def modifyMovie(id, ntitle, ngenre, ndesc, ncopies):
    if id not in movies:
        raise ValueError("Movie ID does not exist!")

    saveMovies()

    movie = movies[id]
    movie.setTitle(ntitle)
    movie.setGenre(ngenre)
    movie.setDesc(ndesc)
    movie.setCopies(ncopies)


def modifyClient(id, nname, ncnp):
    if id not in clients:
        raise ValueError("Client ID does not exist!")

    saveClients()

    client = clients[id]
    client.setName(nname)
    client.setCnp(ncnp)


def modifyRental(id, nmid, ncid, nsdate, nddate):
    if id not in rentals:
        raise ValueError("Rental ID does not exist!")

    saveRentals()

    rental = rentals[id]
    rental.setmId(nmid)
    rental.setcId(ncid)
    rental.setSdate(nsdate)
    rental.setDdate(nddate)


# UNDO OPERATIONS

def undoM():
    global movies

    if not mhistory:
        raise ValueError("Nothing to undo!")

    movies = mhistory.pop()
    return True


def undoC():
    global clients

    if not chistory:
        raise ValueError("Nothing to undo!")

    clients = chistory.pop()
    return True


def undoR():
    global rentals

    if not rhistory:
        raise ValueError("Nothing to undo!")

    rentals = rhistory.pop()
    return True

def setMovies(newMovies):
    global movies
    movies = deepcopy(newMovies)
    mhistory.clear()


def setClients(newClients):
    global clients
    clients = deepcopy(newClients)
    chistory.clear()


def setRentals(newRentals):
    global rentals
    rentals = deepcopy(newRentals)
    rhistory.clear()


def initializeRepository():
    setMovies({})
    setClients({})
    setRentals({})

    Movie.nextId = 1
    Client.nextId = 1
    Rental.nextId = 1

    # MOVIES
    addMovie("Shrek", "Animation", "An ogre's adventure", 12)
    addMovie("The Dark Knight", "Action", "Batman faces the Joker", 8)
    addMovie("Interstellar", "Sci-Fi", "A journey through space", 15)
    addMovie("The Godfather", "Crime", "The Corleone family", 6)
    addMovie("Inception", "Sci-Fi", "Dreams within dreams", 10)
    addMovie("Titanic", "Romance", "A love story aboard the Titanic", 7)
    addMovie("The Matrix", "Sci-Fi", "A hacker discovers reality", 11)
    addMovie("Gladiator", "Action", "A Roman general seeks revenge", 9)
    addMovie("Pulp Fiction", "Crime", "Interconnected criminal stories", 5)
    addMovie("Finding Nemo", "Animation", "A father's ocean adventure", 14)

    # CLIENTS
    addClient("Andrei Popescu", "5010101123456")
    addClient("Maria Ionescu", "6020212123456")
    addClient("Alexandru Marin", "5030313123456")
    addClient("Elena Dumitrescu", "6040414123456")
    addClient("Mihai Georgescu", "5050515123456")
    addClient("Ioana Stan", "6060616123456")

    # RENTALS
    addRental(1, 1, "01/11/2026", "10/11/2026")
    addRental(3, 2, "03/11/2026", "12/11/2026")
    addRental(5, 3, "04/11/2026", "14/11/2026")
    addRental(2, 4, "05/11/2026", "15/11/2026")
    addRental(7, 5, "06/11/2026", "16/11/2026")
    addRental(10, 6, "07/11/2026", "17/11/2026")

    # Initial data should not count as user operations
    mhistory.clear()
    chistory.clear()
    rhistory.clear()
"""
