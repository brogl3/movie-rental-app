from copy import deepcopy
from datetime import date
from helpers import dateToDays
from domain_rentals import Rental


class RentalRepository:
    def __init__(self):
        self._rentals = {}
        self._history = []
        self._next_id = 1

    def setRentals(self, data):
        self._rentals = deepcopy(data)
        self._next_id = max(self._rentals, default=0) + 1
        self._history.clear()

    def _save(self):
        self._history.append(deepcopy(self._rentals))

    def getRentalById(self, id):
        return self._rentals.get(id)
    def getAllRentals(self):
        return list(self._rentals)
    def rentalExists(self, id):
        return id in self._rentals

    def addRental(self, mid, cid, start, due):
        self._save()
        rental = Rental(self._next_id, mid, cid, start, due)
        self._next_id += 1
        self._rentals[rental.getId()] = rental
        return rental

    def deleteRental(self, id):
        if id not in self._rentals:
            raise ValueError('Rental ID does not exist!')
        self._save()
        del self._rentals[id]

    def modifyRental(self, id, mid, cid, start, due):
        rental = self.getRentalById(id)
        if rental is None:
            raise ValueError('Rental ID does not exist!')
        self._save()
        rental.setmId(mid)
        rental.setcId(cid)
        rental.setSdate(start)
        rental.setDdate(due)

    def hasActiveMovieRental(self, mid):
        today = date.today().strftime("%d/%m/%Y")
        today = dateToDays(today)
        for rental in self._rentals.values():
            if rental.getmId() == mid:
                if dateToDays(rental.getSdate()) <= today <= dateToDays(rental.getDdate()):
                    return True
        return False

    def hasActiveClientRental(self, cid):
        today = date.today().strftime("%d/%m/%Y")
        today = dateToDays(today)
        for rental in self._rentals.values():
            if rental.getcId() == cid:
                if dateToDays(rental.getSdate()) <= today <= dateToDays(rental.getDdate()):
                    return True
        return False

    def removeForMovie(self, mid):
        affected = {rid: deepcopy(r) for rid, r in self._rentals.items() if r.getmId() == mid}
        for rid in affected:
            del self._rentals[rid]
        return affected

    def removeForClient(self, cid):
        affected = {rid: deepcopy(r) for rid, r in self._rentals.items() if r.getcId() == cid}
        for rid in affected:
            del self._rentals[rid]
        return affected

    def restoreCascade(self, affected):
        # Do not overwrite a rental that might have appeared in the meantime.
        collisions = set(affected).intersection(self._rentals)
        if collisions:
            raise ValueError(f'Cannot restore rentals; IDs already exist: {sorted(collisions)}')
        self._rentals.update(deepcopy(affected))

    def undoR(self):
        if not self._history:
            raise ValueError('Nothing to undo!')
        self._rentals = self._history.pop()
        return True
