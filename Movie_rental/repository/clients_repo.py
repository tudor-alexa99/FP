from domain.client import Client
from iterable.iter import Iterable


class Clients_Repository:
    def __init__(self):
        self._clientList = []
        #if populate == True:
        #    self.initialize()

    # def initialize(self):
    #     self.add(Client("George", 10))
    #     self.add(Client("Sabina", 11))
    #     self.add(Client("Alex", 12))
    #     self.add(Client("Josh", 13))
    #     self.add(Client("Martin", 14))
    #     self.add(Client("Erika", 15))
    #     self.add(Client("Patricia", 16))

    def add(self, new_client):
        self._clientList.append(new_client)

    def __getitem__(self, item):
        return self._clientList[item]

    # def remove(self, id):
    #     i = 0
    #     for client in self.__clientList:
    #         if client.id() == id:
    #             self.__clientList.pop(i)
    #         i += 1
    def remove(self, pos):
        self._clientList.pop(pos)


    def getAll(self):
        return self._clientList

    def find_by_id(self, id):
        for client in self._clientList:
            if client.id == id:
                return True
        return False
    def delete_id(self, id):
        i = 0
        for client in self._clientList:
            if client.id == id:
                self.remove(i)
            i += 1
    def __len__(self):
        return len(self._clientList)
    # def update(self, id, new_name):
    #     for client in self._clientList:
    #         if client.id == id:
    #             client.set_name(new_name)


    # def update(self, id, new_name):
    #     for client in self.__clientList:
    #         if client.id == id:
    #             client.set_name(new_name)
    #controller

    # def get_position(self, id):
    #     i = 0
    #     for client in self.__clientList:
    #         if client.id == id:
    #             return i
    #         i += 1
    #controller
    # def toString(self):
    #     lst = []
    #     for client in self.__clientList:
    #         lst.extend(client.toString())
    #     return lst
    #controller