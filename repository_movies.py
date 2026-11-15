from copy import deepcopy
from domain_movie import Movie



class Movies:

    def __init__(self):
        self.nextId = 1
        self._movies = {}
        self._history = []

    def snapshot(self):
        return deepcopy(self._movies)

    def save(self):
        self._history.append(self.snapshot())

    def addMovie(self, title, genre, desc, copies):
        movie = Movie(self.nextId, title, genre, desc, copies)
        self._movies[self.nextId] = movie
        self.nextId += 1

    def movieExists(self, id):
        return id in self._movies

    def getMovieById(self, id):
        return self._movies.get(id)

    def getAllMovies(self):
        return list(self._movies)

    def deleteMovie(self, id):
        if not self.movieExists(id):
            raise ValueError("No movie with such ID exists!")
        else:
            self.save()
            del self._movies[id]

    def modifyMovie(self, id, ntitle, ngenre, ndesc, ncopies):
        if not self.movieExists(id):
            raise ValueError("No movie with such ID exists!")
        else:
            self.save()
            movie = getMovieById(id)
            movie.setTtitle(ntitle)
            movie.setGenre(ngenre)
            movie.setDesc(ndesc)
            movie.setCopies(ncopies)

    def undoM(self):
        if not self._history:
            raise ValueError("Nothing to undo!")
        else:
            self._movies = self._history.pop

    def setMovies(self, data):
        self._movies = deepcopy(data)
        self.nextId = max(self._movies, default=0) + 1
        self._history = []
