class Rental:
    def __init__(self, id: int, mId: int, cId: int, sDate: str, dDate: str):
        self.__id = id
        self.__mId = mId
        self.__cId = cId
        self.__sDate = sDate
        self.__dDate = dDate

    def __str__(self):
        return f" [{self.__id}] | Client with ID: [{self.__cId}] rented movie with ID: [{self.__mId}] from {self.__sDate} until {self.__dDate}"

    def __repr__(self):
        return str(self)
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
    def setmId(self, mId):
        self.__mId = mId
    def setcId(self, cId):
        self.__cId = cId
    def setSdate(self, sDate):
        self.__sDate = sDate
    def setDdate(self, dDate):
        self.__dDate = dDate
