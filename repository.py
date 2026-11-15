from repository_movies import MovieRepository
from repository_clients import ClientRepository
from repository_rentals import RentalRepository


class RepositoryManager:
    def __init__(self):
        self.movies = MovieRepository()
        self.clients = ClientRepository()
        self.rentals = RentalRepository()

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

        # Sample data should not count as user actions.
        self.movies._history.clear()
        self.clients._history.clear()
        self.rentals._history.clear()
