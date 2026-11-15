class Client:
    def __init__(self, id: int, name: str, cnp: str):
        self.__id = id
        self.__name = name
        self.__cnp = cnp

    def __str__(self):
        return f" [{self.__id}] | Name: {self.__name} | CNP: {self.__cnp}"

    def __repr__(self):
        return str(self)
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getCnp(self):
        return self.__cnp
    def setName(self, name):
        self.__name = name
    def setCnp(self, cnp):
        self.__cnp = cnp
