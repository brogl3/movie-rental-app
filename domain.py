
class Movie:
    nextId = 1

    def __init__(self, title: str, genre: str, desc: str, copies: int):
        self.__id = Movie.nextId
        Movie.nextId += 1
        self.__title = title
        self.__genre = genre
        self.__desc = desc
        self.__copies = copies

    def __str__(self):
        return f" [{self.__id}] | {self.__title} | Genre: {self.__genre} | Description: {self.__desc} | {self.__copies} copies available"

    def __repr__(self):
        return self.__str__()

    # Getters
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

    # Setters
    def setTitle(self, title):
        self.__title = title

    def setGenre(self, genre):
        self.__genre = genre

    def setDesc(self, desc):
        self.__desc = desc

    def setCopies(self, copies):
        self.__copies = copies


class Client:
    nextId = 1

    def __init__(self, name: str, cnp: str):
        self.__id = Client.nextId
        Client.nextId += 1
        self.__name = name
        self.__cnp = cnp

    def __str__(self):
        return f" [{self.__id}] | Name: {self.__name} | CNP: {self.__cnp}"

    def __repr__(self):
        return self.__str__()

    # Getters
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCnp(self):
        return self.__cnp

    # Setters
    def setName(self, name):
        self.__name = name

    def setCnp(self, cnp):
        self.__cnp = cnp


class Rental:
    nextId = 1

    def __init__(self, mId: int, cId: int, sDate: str, dDate: str):
        self.__id = Rental.nextId
        Rental.nextId += 1
        self.__mId = mId
        self.__cId = cId
        self.__sDate = sDate
        self.__dDate = dDate

    def __str__(self):
        return f" [{self.__id}] | Client with ID: [{self.__cId}] rented movie with ID: [{self.__mId}] from {self.__sDate} until {self.__dDate}"

    def __repr__(self):
        return self.__str__()

    # Getters
    def getId(self):
        return self.__id

    def getmId(self):
        return self.__mId

    def getcId(self):
        return self.__cId

    def getSdate(self):
        return self.__sDate

    def getDdate(self):
        return self.__dDate

    # Setters
    def setmId(self, mId):
        self.__mId = mId

    def setcId(self, cId):
        self.__cId = cId

    def setSdate(self, sDate):
        self.__sDate = sDate

    def setDdate(self, dDate):
        self.__dDate = dDate
