from copy import deepcopy
from domain_movies import Movie


class MovieRepository:
    def __init__(self):
        self._movies = {}
        self._history = []
        self._next_id = 1

    def setMovies(self, data):
        self._movies = deepcopy(data)
        self._next_id = max(self._movies, default=0) + 1
        self._history.clear()

    def snapshot(self):
        return deepcopy(self._movies)

    def _save(self, related_rentals=None):
        # A deletion can record its dependent rentals for atomic undoM.
        self._history.append((self.snapshot(), related_rentals))

    def getMovieById(self, id):
        return self._movies.get(id)
    def getAllMovies(self):
        return list(self._movies)
    def movieExists(self, id):
        return id in self._movies

    def addMovie(self, title, genre, desc, copies):
        self._save()
        movie = Movie(self._next_id, title, genre, desc, copies)
        self._next_id += 1
        self._movies[movie.getId()] = movie
        return movie

    def deleteMovie(self, id, rental_repository=None):
        if id not in self._movies:
            raise ValueError('Movie ID does not exist!')
        if rental_repository is None:
            raise ValueError("Rental repository is required to delete a movie!")
        if rental_repository.hasActiveMovieRental(id):
            raise ValueError("Cannot delete movie: it is currently rented!")
        affected = rental_repository.removeForMovie(id)
        self._save(affected)
        del self._movies[id]

    def modifyMovie(self, id, title, genre, desc, copies):
        movie = self.getMovieById(id)
        if movie is None:
            raise ValueError('Movie ID does not exist!')
        self._save()
        movie.setTitle(title)
        movie.setGenre(genre)
        movie.setDesc(desc)
        movie.setCopies(copies)

    def undoM(self, rental_repository=None):
        if not self._history:
            raise ValueError('Nothing to undo!')
        state, affected = self._history[-1]
        if affected and rental_repository is None:
            raise ValueError('Rental repository required to undo this deletion!')
        if affected:
            rental_repository.restoreCascade(affected)
        self._movies = deepcopy(state)
        self._history.pop()
        return True
