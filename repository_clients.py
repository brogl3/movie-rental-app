from copy import deepcopy
from domain_clients import Client


class ClientRepository:
    def __init__(self):
        self._clients = {}
        self._history = []
        self._next_id = 1

    def setClients(self, data):
        self._clients = deepcopy(data)
        self._next_id = max(self._clients, default=0) + 1
        self._history.clear()

    def _save(self, related_rentals=None):
        self._history.append((deepcopy(self._clients), related_rentals))

    def getClientById(self, id):
        return self._clients.get(id)
    def getAllClients(self):
        return list(self._clients)
    def clientExists(self, id):
        return id in self._clients

    def addClient(self, name, cnp):
        self._save()
        client = Client(self._next_id, name, cnp)
        self._next_id += 1
        self._clients[client.getId()] = client
        return client

    def deleteClient(self, id, rental_repository=None):
        if id not in self._clients:
            raise ValueError('Client ID does not exist!')
        if rental_repository is None:
            raise ValueError("Rental repository is required to delete a client!")
        if rental_repository.hasActiveClientRental(id):
            raise ValueError("Cannot delete client: they currently rent a movie!")
        affected = rental_repository.removeForClient(id)
        self._save(affected)
        del self._clients[id]

    def modifyClient(self, id, name, cnp):
        client = self.getClientById(id)
        if client is None:
            raise ValueError('Client ID does not exist!')
        self._save()
        client.setName(name)
        client.setCnp(cnp)

    def undoC(self, rental_repository=None):
        if not self._history:
            raise ValueError('Nothing to undo!')
        state, affected = self._history[-1]
        if affected and rental_repository is None:
            raise ValueError('Rental repository required to undo this deletion!')
        if affected:
            rental_repository.restoreCascade(affected)
        self._clients = deepcopy(state)
        self._history.pop()
        return True
