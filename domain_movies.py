class Movie:
    def __init__(self, id: int, title: str, genre: str, desc: str, copies: int):
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__desc = desc
        self.__copies = copies

    def __str__(self):
        return f" [{self.__id}] | {self.__title} | Genre: {self.__genre} | Description: {self.__desc} | {self.__copies} copies available"

    def __repr__(self):
        return str(self)

    def getId(self):
        return self.__id
    def getTitle(self):
        return self.__title
    def getGenre(self):
        return self.__genre
    def getDesc(self):
        return self.__desc
    def getCopies(self):
        return self.__copies
    def setTitle(self, title):
        self.__title = title
    def setGenre(self, genre):
        self.__genre = genre
    def setDesc(self, desc):
        self.__desc = desc
    def setCopies(self, copies):
        self.__copies = copies
