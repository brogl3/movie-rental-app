from repository import RepositoryManager

class commandHandler():
    def __init__(self, repos):
        self.repos = repos
    #(command, expected arguments, types of arguments)

        self.commands = {
            "help": (self.help, 0, ""),
            "exit": (self.endProgram, 0, ""),
            "add movie": (self.addM, 4, "NNNI"),
            "delete movie": (self.deleteM, 1, "m"),
            "edit movie": (self.editM, 5, "mNNNI"),
            "add client": (self.addC, 2, "NN"),
            "delete client": (self.deleteC, 1, "c"),
            "edit client": (self.editC, 3, "cNN"),
            "add rental": (self.addR, 4, "mcP"),
            "delete rental": (self.deleteR, 1, "r"),
            "edit rental": (self.editR, 5, "rmcP"),
            "undoR": (self.undoRc, 0, ""),
            "undoM": (self.undoMc, 0, ""),
            "undoC": (self.undoCc, 0, ""),
            "show movies": (self.showMovies, 0, ""),
            "show clients": (self.showClients, 0, ""),
            "show rentals": (self.showRentals, 0, "")
        }

    def help(self):
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
            show movies #shows all the movies
            show clients #shows all the clients
            show rentals #guess what it does?
            """)

    def executeCommand(self, cmd, args):
        return self.commands[cmd][0](*args)

    def endProgram(self):
        print("Talofa!")
        exit()

    def addM(self, title, genre, desc, copies):
        self.repos.movies.addMovie(title, genre, desc, copies)

    def deleteM(self, id):
        self.repos.movies.deleteMovie(id, self.repos.rentals)
        print("Movie deleted successfully!")

    def editM(self, id, ntitle, ngenre, ndesc, ncopies):
        self.repos.movies.modifyMovie(id, ntitle, ngenre, ndesc, ncopies)
        print("Movie edited successfully!")

    def addC(self, name, cnp):
        self.repos.clients.addClient(name, cnp)
        print("Client added successfully!")

    def deleteC(self, id):
        self.repos.clients.deleteClient(id, self.repos.rentals)
        print("Client deleted successfully!")

    def editC(self, id, nname, ncnp):
        self.repos.clients.modifyClient(id, nname, ncnp)
        print("Client edited successfully!")

    def addR(self, m, c, sd, dd):
        self.repos.rentals.addRental(m, c, sd, dd)
        print("Rental added successfully!")

    def deleteR(self, id):
        self.repos.rentals.deleteRental(id)
        print("Rental deleted successfully!")

    def editR(self, id, m, c, sd, dd):
        self.repos.rentals.modifyRental(id, m, c, sd, dd)
        print("Rental edited successfully!")

    def undoMc(self):
        return self.repos.movies.undoM(self.repos.rentals)

    def undoCc(self):
        return self.repos.clients.undoC(self.repos.rentals)

    def undoRc(self):
        return self.repos.rentals.undoR()

    def getParams(self, cmd):
        return self.commands[cmd][1], self.commands[cmd][2]

    def getCommands(self):
        return list(self.commands.keys())

    def showMovies(self):
        movies = self.repos.movies.getAllMovies()
        for id in movies:
            print(self.repos.movies.getMovieById(id))

    def showClients(self):
        clients = self.repos.clients.getAllClients()
        for id in clients:
            print(self.repos.clients.getClientById(id))

    def showRentals(self):
        rentals = self.repos.rentals.getAllRentals()
        for id in rentals:
            print(self.repos.rentals.getRentalById(id))








