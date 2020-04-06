#from repository.clients_repo import Clients_Repository
from iterable.iter import Iterable, shellSort
from domain.client_validator import ValidateClient
from domain.client import Client
from repository.clients_repo import Clients_Repository
from controller.undo_controller import *
from controller.rental_controller import Rental_Repository
class ClientController():
    def __init__(self,undo_controller,client_repo,rental_repo,setup = True ):
        self._clientList = client_repo
        self._validator = ValidateClient()
        self._undoController = undo_controller
        self._rentalsList = rental_repo
        if setup == True:
            self.initialize()

    def create(self, clientId, name):
        """
        Takes a new clientId and name, checks to see if the id is already in use or not
        and adds the client to thelist or raises an error
        """
        if self.find_by_id(clientId)  == True:
            raise NameError
        client = Client(name, clientId)
        self._validator.validate(client)
        self._clientList.add(client)
        #pick the undo and redo functions
        undo = FunctionCall(self.remove, clientId)
        redo = FunctionCall(self.create, clientId, name)
        #save them as an operation
        operation = Operation(undo, redo)

        self._undoController.addOperation(operation)


    def initialize(self):
        """

        Initialises the list with 50 clients
        """
        self._clientList.add(Client("George", 10))
        self._clientList.add(Client("Sabina", 11))
        self._clientList.add(Client("Alex", 12))
        self._clientList.add(Client("Josh", 13))
        self._clientList.add(Client("Martin", 14))
        self._clientList.add(Client("Erika", 15))
        self._clientList.add(Client("Patricia", 16))
        self._clientList.add(Client("Miguel",17 ))
        self._clientList.add(Client("Narcos",18 ))
        self._clientList.add(Client("Enrique",19 ))
        self._clientList.add(Client("Iziquel",20 ))
        self._clientList.add(Client("Audrey",21 ))
        self._clientList.add(Client("Anrei",22 ))
        self._clientList.add(Client("Alexandria",23 ))
        self._clientList.add(Client("Laquisha",24 ))
        self._clientList.add(Client("YoMamma",25 ))
        self._clientList.add(Client("Anotnia", 26))
        self._clientList.add(Client("Iris", 27))
        self._clientList.add(Client("Henderson", 28))
        self._clientList.add(Client("Christian", 29))
        self._clientList.add(Client("Negan",30 ))
        self._clientList.add(Client("Carol",31 ))
        self._clientList.add(Client("Carla", 32))
        self._clientList.add(Client("Theodor",33 ))
        self._clientList.add(Client("Peter", 34))
        self._clientList.add(Client("Amber",35 ))
        self._clientList.add(Client("PreafericitulDaniel", 36))
        self._clientList.add(Client("Pastore", 37))
        self._clientList.add(Client("Cristiano",38 ))
        self._clientList.add(Client("Ronaldo",39 ))
        self._clientList.add(Client("Messi",40 ))
        self._clientList.add(Client("Maradonna",41 ))
        self._clientList.add(Client("Gerald",42))
        self._clientList.add(Client("Insigne",43 ))
        self._clientList.add(Client("Purandelinho",44 ))
        self._clientList.add(Client("Ion_a_lu_Glanetasu",45 ))
        self._clientList.add(Client("Ana",46 ))
        self._clientList.add(Client("Are Mere",47 ))
        self._clientList.add(Client("Adam",48 ))
        self._clientList.add(Client("Levine",49 ))
        self._clientList.add(Client("Bruno",50 ))
    def remove(self, id):
        """
        Finds the position (in the repo) of the client that has the given id and removes it
        """
        co = CascadedOperation()
        pos = 0
        for client in self._clientList:
            if client.id == id:

                undo = FunctionCall(self.create, client.id,client.name)
                redo = FunctionCall(self.remove, client.id)
                operation = Operation(undo, redo)
                co.add(operation)
                self._clientList.remove(pos)
            pos += 1
        pos = 0
        while pos < len(self._rentalsList.getAll()):
        #for pos in range(0, len(self._rentalsList.getAll())):
            if self._rentalsList[pos].clientId == id:
                undo = FunctionCall(self._rentalsList.create_rental, self._rentalsList[pos].rentalId, self._rentalsList[pos].movieId, self._rentalsList[pos].clientId, self._rentalsList[pos].rented_date, self._rentalsList[pos].due_date, self._rentalsList[pos].returned_date)
                redo = FunctionCall(self._rentalsList.remove_by_clientId, id)
                operation = Operation(undo, redo)
                co.add(operation)
                self._rentalsList.remove_by_clientId(self._rentalsList[pos].clientId)
                #is_deleted = True:
            else:
                pos += 1
        self._undoController.addOperation(co)

    def find_by_id(self,id):
        """
        Searches in the list to see if the given id is already in use or not
        :return: True, if the id is in use
                 False, is contrary
        """
        for client in self._clientList:
            if client.id == id:
                return True
        return False

    def get_position(self, id):
        """
        searches for the position of a client with the given id
        :return: position
        """
        i = 0
        for client in self._clientList:
            if client.id == id:
                return i
            i += 1

    def getAll(self):
        return self._clientList.getAll()

    def update(self, id, new_name):
        for client in self._clientList:
            if client.id == id:
                client.set_name(new_name)
    def toString(self):
        """
        Function used for the 'Search' application
        Returns all the clients in the list as a list of strings
        (each "word" is a separate element in the list)
        """
        lst = []
        for client in self._clientList:
            lst.extend(client.toString())
        return lst

    def __getitem__(self, item):
        """
        Used for indexing the clientsList
        """
        return self._clientList[item]

    def add(self, c1):
        if self.find_by_id(c1.id) == True:
            raise NameError
        self._clientList.add(c1)

    # def shellSort(self, _list, key=lambda x: x):
    #     gap = len(_list) // 2
    #     while gap > 0:
    #         for start in range(gap):
    #             for i in range(start + gap, len(_list), gap):
    #
    #                 currentvalue = _list[i]
    #                 # currentvalue = key(_list[i])
    #                 position = i
    #
    #                 while position >= gap and key(_list[position - gap]) < key(currentvalue):
    #                     _list[position] = _list[position - gap]
    #                     position = position - gap
    #
    #                 _list[position] = currentvalue
    #         gap = gap // 2


import unittest
class Test_Clients(unittest.TestCase):
    def setUp(self):
        self.clientsList = ClientController(False)
        c1 = Client("George", 10)
        c2 = Client("Dennis", 11)
        c3 = Client("Abigail", 12)
        c4 = Client("Joshua", 12) #

    def test_create(self):
        #self.clientsList = ClientController(False)
        self.clientsList.create(10,"Dennis")
        self.clientsList.create( 11,"Joshua")
        self.assertRaises(NameError, self.clientsList.create, 11, "Abigail")
        self.assertEqual(len(self.clientsList.getAll()), 2)

    def test_update(self):
        c1 = Client("George", 10)
        self.clientsList.add(c1)
        self.clientsList.update(10, "Danny")
        self.assertEqual(c1.name, "Danny")

def check_this_out():
    control  = ClientController(False)
    #c1 = Client("George", 12)
    control.create(12,"George")
    control.create(13, "Dennis")
    control.create(14, "Chriss")
    #control._undoController.undo()
    print(control.toString())
    control.remove(12)
    print(control.toString())
    control._undoController.undo()
    # control._undoController.redo()
    print(control.toString())
    #print(control.toString())
#check_this_out()

