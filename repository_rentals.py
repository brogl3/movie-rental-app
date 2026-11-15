
from copy import deepcopy
from domain_rental import Rental


class Rentals:

    def __init__(self):
        self.nextId = 1
        self._rentals = {}
        self._history = []

    def snapshot(self):
        return deepcopy(self._rentals)

    def save(self):
        self._history.append(self.snapshot())

    def addRental(self, mid, cid, sdate, ddate):
        rental = Rental(self.nextId, mid, cid, sdate, ddate)
        self._rentals[self.nextId] = rental
        self.nextId += 1

    def rentalExists(self, id):
        return id in self._rentals

    def getRentalById(self, id):
        return self._rentals.get(id)

    def getAllRentals(self):
        return list(self._rentals)

    def deleteRental(self, id):
        if not self.rentalExists(id):
            raise ValueError("No rental with such ID exists!")
        else:
            self.save()
            del self._rentals[id]

    def modifyRental(self, id, nmid, ncid, nsdate, nddate):
        if not self.rentalExists(id):
            raise ValueError("No rental with such ID exists!")
        else:
            self.save()
            rental = self._rentals[id]
            rental.setmId(nmid)
            rental.setcId(ncid)
            rental.setSdate(nsdate)
            rental.setDdate(nddate)

    def undoR(self):
        if not self._history:
            raise ValueError("Nothing to undo!")
        else:
            self._rentals = self._history.pop()
            return True

    def setRentals(self, data):
        self._clients = deepcopy(data)
        self.nextId = max(self._clients, default=0) + 1
        self._history = []