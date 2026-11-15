from copy import deepcopy
from domain_client import Client


class Clients:

    def __init__(self):
        self.nextId = 1
        self._clients = {}
        self._history = []

    def snapshot(self):
        return deepcopy(self._clients)

    def save(self):
        self._history.append(self.snapshot())

    def addClient(self, name, cnp):
        client = Client(self.nextId, name, cnp)
        self._clients[self.nextId] = client
        self.nextId += 1

    def clientExists(self, id):
        return id in self._clients

    def getClientById(self, id):
        return self._clients.get(id)

    def getAllClients(self):
        return list(self._clients)

    def deleteClient(self, id):
        if not self.clientExists(id):
            raise ValueError("No client with such ID exists!")
        else:
            self.save()
            del self._clients[id]

    def modifyClient(self, id, nname, ncnp):
        if not self.clientExists(id):
            raise ValueError("No client with such ID exists!")
        else:
            self.save()
            client = self._clients[id]
            client.setName(nname)
            client.setCnp(ncnp)

    def undoC(self):
        if not self._history:
            raise ValueError("Nothing to undo!")
        else:
            self._clients = self._history.pop()
            return True

    def setClients(self, data):
        self._clients = deepcopy(data)
        self._nextId = max(self._clients, default=0) + 1
        self._history = []