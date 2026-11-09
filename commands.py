from repository import addMovie, deleteMovie, modifyMovie, addClient, deleteClient, modifyClient, addRental, \
    deleteRental, modifyRental, undoM, undoC, undoR, getAllMovies, getMovieById, getAllClients, getClientById, \
    getAllRentals, getRentalById


def help():
    print("""
    help - it's this one!
    exit #exits the program
    add movie; [title]; [genre]; [desc]; [copies]
    delete movie; [id]
    edit movie; [id]; [new title]; [new genre]; [new desc]; [new copies]
    add client; [name]; [cnp]
    delete client; [id]
    edit client; [id]; [name]; [cnp]
    add rental; [rented movie ID]; [client ID]; [start date]; [due date] #dates must be in the dd/mm/yyyy format!
    delete rental; [id]
    edit rental; [id]; [new movie ID]; [new client ID]; [new start date]; [new due date]
    undoM #undoes the last operation done on movies
    undoC #undoes the last operation done on clients
    undoR #undoes the last operation done on rentals
    """)

def endProgram():
    print("Talofa!")
    exit()

def addM(title, genre, desc, copies):
    addMovie(title, genre, desc, copies)
    print("Movied added successfully!")

def deleteM(id):
    deleteMovie(id)
    print("Movied deleted successfully!")

def editM(id, ntitle, ngenre, ndesc, ncopies):
    modifyMovie(id, ntitle, ngenre, ndesc, ncopies)
    print("Movied edited successfully!")

def addC(name, cnp):
    addClient(name, cnp)
    print("Client added successfully!")

def deleteC(id):
    deleteClient(id)
    print("Client deleted successfully!")

def editC(id, nname, ncnp):
    modifyClient(id, nname, ncnp)
    print("Client edited successfully!")

def addR(m, c, sd, dd):
    addRental(m, c, sd, dd)
    print("Rental added successfully!")

def deleteR(id):
    deleteRental(id)
    print("Rental deleted successfully!")

def editR(id, m, c, sd, dd):
    modifyRental(id, m, c, sd, dd)
    print("Rental edited successfully!")

def undoMc():
    if not undoM():
        raise ValueError("Nothing to undo!")



def undoCc():
    if not undoC():
        raise ValueError("Nothing to undo!")

def undoRc():
    if not undoR():
        raise ValueError("Nothing to undo!")

def getParams(cmd):
    return commands[cmd][1], commands[cmd][2]

def getCommands():
    return list(commands.keys())

def showMovies():
    movies = getAllMovies()
    for id in movies:
        print(getMovieById(id))

def showClients():
    clients = getAllClients()
    for id in clients:
        print(getClientById(id))

def showRentals():
    rentals = getAllRentals()
    for id in rentals:
        print(getRentalById(id))


# (command, expected arguments, types of arguments)
commands = {
    "help": (help, 0, ""),
    "exit": (endProgram, 0, ""),
    "add movie" : (addM, 4, "NNNI"),
    "delete movie" : (deleteM, 1, "m"),
    "edit movie": (editM, 5, "mNNNI"),
    "add client": (addC, 2, "NN"),
    "delete client": (deleteC, 1, "c"),
    "edit client": (editC, 3, "cNN"),
    "add rental": (addR, 4, "mcP"),
    "delete rental": (deleteR, 1, "r"),
    "edit rental": (editR, 5, "rmcP"),
    "undoR": (undoRc, 0, ""),
    "undoM": (undoMc, 0, ""),
    "undoC": (undoCc, 0, ""),
    "show movies" : (showMovies, 0, ""),
    "show clients" : (showClients, 0, ""),
    "show rentals" : (showRentals, 0, "")


}

def executeCommand(cmd, args):
    return commands[cmd][0](*args)

