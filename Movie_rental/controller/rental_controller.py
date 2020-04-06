from controller.undo_controller import FunctionCall, Operation
from domain.rental import Rental
from iterable.iter import shellSort
from repository.rental_repo import Rental_Repository
#from controller.movie_controller import MovieController
#from controller.client_controller import ClientController
from datetime import datetime
from datetime import timedelta


class RentalController:
    def __init__(self, rental_repo, undo_controller ,  nonempty = True):
        self.__rentalList = rental_repo
        self.__undo_controller = undo_controller
        if nonempty == True:
            self.initialise()

    def add(self, new_rental):
        """
        Adds a new rental to the list
        """
        undo = FunctionCall(self.remove_by_clientId, new_rental.clientId)
        redo = FunctionCall(self.add, new_rental)
        op = Operation(undo, redo)
        self.__undo_controller.addOperation(op)

        self.__rentalList.add(new_rental)

    def remove_by_clientId(self, clientID):
        """
        Searches for the position of the client with the given id
        and removes all the rentals of the client
        """
        pos = 0
        for rent in self.__rentalList:
            if rent.clientId == clientID:
                self.__rentalList.remove(pos)
            pos += 1

    def rent(self,rentalId, clientId, movieId, n, client_repo,movie_repo):
        """
        Creates a new rental with the given parameters
        The function checks if the movie is available (either has not been rented or the return dat is set != None
        Takes the number of days for the rental and uses it to create a due_date
        """
        returned_date = None # None
        # fa-l input cu numarul de zile
        rented_date = datetime.now()
        due_date = datetime.now() + timedelta(days = n)
        print(clientId, movieId, client_repo.get_position(clientId))

        if client_repo.find_by_id(clientId) :
            if movie_repo.find_by_id(movieId) == True:
                client = client_repo[client_repo.get_position(clientId)]
                movie = movie_repo[movie_repo.get_position(movieId)]

                print("The Client:", client.name, "rented the movie: ", movie.title, " ")
                rental = Rental(rentalId, movie.id, client.id, rented_date, due_date, returned_date)



                undo = FunctionCall(self.remove_by_clientId, self.__rentalList.size()-1)
                redo = FunctionCall(self.add, rental)
                op = Operation(undo, redo)
                self.__undo_controller.addOperation(op)

                self.__rentalList.add(rental)

    def find_by_id(self, id):
        """
        Searches for the position of the rental, using the rantalId
        Either returns the position, or "False" if 'found' is equal to 0
        """
        i = 0
        found = 0
        for rent in self.__rentalList:
            if rent.rentalId == id:
                found = 1
                return i
            i += 1
        if found == 0:
            return False

    def _return(self, pos):
        """
        Function for returning a movie
        The returned_date is set to datetime.now()
        """
        returned_date = datetime.now()
        self.__rentalList[pos].set_returned_date(returned_date)
        undo = FunctionCall(self.__rentalList[pos].set_returned_date, None)
        redo = FunctionCall(self.__rentalList[pos].set_returned_date,datetime.now())
        operation = Operation(undo, redo)
        self.__undo_controller.addOperation(operation)

    def getAll(self):
        return self.__rentalList.getAll()

    def check_valid_client(self, clientId):
        """
        Checks in the list of rentals whether a client has not returned a movie yet
        If so, the functin returns False and prevents the rental from taking place
        In the other case, it returns True (meaning that the client is valid)
        """
        for rental in self.__rentalList:
            if rental.clientId == clientId and (rental.returned_date == None and rental.due_date < datetime.now()):
                return False
        return True

    def __getitem__(self, item):
        return self.__rentalList[item]

    def last_id(self):
        """
        Used for generating the rentalId's consecutively
        Takes the last id from the rentalsList (if non-empty) and adds 1
        Returns the new id
        """
        if self.__rentalList.size() == 0:
            return 0
        else:
            return self.__rentalList[-1].rentalId + 1

    def list_rentals(self):
        # for rent in self.__rentalList:
        #    print(rent, "\n")
        for i in range(0, self.__rentalList.size()):
            print(self.__rentalList[i])

    def check_available_movie(self, id):
        """
        Checks all the movies rented in the rentalsList
        If a movie's returned_date is set to None, it means it was not returned
        If a movie's id is not in the list, it means it it available
        Returns True of False accordingly
        """
        for rental in self.__rentalList:
            if rental.movieId == id:
                if rental.returned_date == None:
                    return False
        return True
    #
    # def movieTitle(self, id):
    #     for rent in self.__rentalList:
    #         if rent.movieId == id:
    def most_rented_movies(self):
        """
        Searches in the rentalList for the movieId's that appear the most
        Saves them in a dictionary (key = movieId, value = numb_of_aparitions)
        Takes all the items in the dictionary and saves them in a new list, sorted by the number of aparitions
        Returns the new, sorted list
        """
        movies = {}
        for rent in self.__rentalList:
            if rent.movieId in movies.keys():
                movies[rent.movieId] += 1
            else:
                movies[rent.movieId] = 1
        #most_rented = sorted(movies.items(),key = lambda item:item[1], reverse = True)
        #print (movies.items())
        items = list(movies.items())
        for i in range(len(items)):
            items[i] = list(items[i])
        #print(items)
        #most_rented = items
        shellSort(items,lambda item:item[1])
        # reversed(items)
        return items

    def most_active_clients(self):
        """
        Searches in the rentalList for the clientId's that appear the most
        Saves them in a dictionary (key = clientId, value = numb_of_aparitions)
        Takes all the items in the dictionary and saves them in a new list, sorted by the number of aparitions
        Returns the new, sorted list
        """

        clients = {}
        #make it a dictionary
        for rent in self.__rentalList:
            if rent.clientId in clients.keys():
                if rent.returned_date != None: # cjeck to see if they've returned the movie yet or not
                    clients[rent.clientId] += (rent.returned_date - rent.rented_date).days
                else:
                    clients[rent.clientId] += (datetime.now() - rent.rented_date).days
            else:
                if rent.returned_date != None:
                    clients[rent.clientId] = (rent.returned_date - rent.rented_date).days
                else:
                    clients[rent.clientId] = (datetime.now() - rent.rented_date).days
        most_active = sorted(clients.items(),key = lambda item:item[1], reverse = True)
        return most_active


    def initialise(self):
        r1 = Rental(1, 100, 10, datetime(2018, 3, 10), datetime(2018, 3, 20), None)
        r2 = Rental(2, 101, 11, datetime(2018, 4, 12), datetime(2018,12, 20), None)
        r3 = Rental(3, 102, 12, datetime(2018, 5, 12), datetime(2018,12, 20),datetime(2018, 10, 22))
        r4 = Rental(4, 103, 12, datetime(2018, 10, 24), datetime(2018,11, 20),None)
        r5 = Rental(5, 110, 21, datetime(2018, 11, 22), datetime(2018,12, 20),None)
        r6 = Rental(6, 111, 26, datetime(2018, 11, 25), datetime(2018,11, 26),None)
        r7 = Rental(7, 112, 28, datetime(2018, 11, 24), datetime(2018,11, 25), datetime(2018,11, 26))
        r8 = Rental(8, 113, 20, datetime(2018, 11, 25), datetime(2018,11, 27), datetime(2018,11, 26))
        r9 = Rental(9, 102, 29, datetime(2018, 10, 10), datetime(2018,11, 11), datetime(2018,11, 26))
        r10= Rental(10, 130, 20, datetime(2018, 4, 25), datetime(2018,5, 27), datetime(2018,5, 26))
        r11= Rental(11, 112, 22, datetime(2018, 9, 4), datetime(2018,11, 5), None)
        r12= Rental(12, 113, 20, datetime(2018, 10, 30), datetime(2018,11, 2), datetime(2018,11, 2))
        r13= Rental(14, 105, 16, datetime(2018, 10, 29), datetime(2018,11, 29), None)
        self.add(r1)
        self.add(r2)
        self.add(r3)
        self.add(r4)
        self.add(r5)
        self.add(r6)
        self.add(r7)
        self.add(r8)
        self.add(r9)
        self.add(r10)
        self.add(r11)
        self.add(r12)
        self.add(r13)

        # self.__rentalList.add(r2)
        # self.__rentalList.add(r3)
        # self.__rentalList.add(r4)
        # self.__rentalList.add(r5)
        # self.__rentalList.add(r6)
        # self.__rentalList.add(r7)
        # self.__rentalList.add(r8)
        # self.__rentalList.add(r9)
        # self.__rentalList.add(r10)
        # self.__rentalList.add(r11)
        # self.__rentalList.add(r12)
        # self.__rentalList.add(r13)

    def late_returns(self):
        """
        Takes all the rentlas in rentalsList and checks whether the movie has been returned past the due_date or has not yet
        been returned and the due_date has passed
        Adds them to a dctionary, sorts them by the num of aparitions, returns them as a list
        """
        returns = {}
        for rent in self.__rentalList:
            if rent.returned_date != None:
                if rent.due_date <= datetime.now():
                    if rent.movieId in returns.keys():
                        returns[rent.movieId] += (datetime.now() - rent.due_date).days
                    else:
                        returns[rent.movieId] = (datetime.now() - rent.due_date).days
        late_returns = sorted(returns.items(),key = lambda item:item[1], reverse = True)
        return late_returns
#
# def test_find_by_id():
#     lst = Rental_Repository([],[])
#     lst.initialize()
#     assert lst.find_by_id(1) == 0 ,"Something's wrong"
#     #print (lst.find_by_id(2))
#     assert lst.find_by_id(1000) == False , "Oops"

import unittest

class Test_Statistics(unittest.TestCase):
    def setUp(self):
        self.rentalsList = RentalController(False)
        r1 = Rental(90, 106 , 10, None, datetime(2018, 3, 10), None)
        r2 = Rental(91, 100, 11)
        r3 = Rental(92, 106, 12)
        self.rentalsList.add(r1)
        self.rentalsList.add(r2)
        self.rentalsList.add(r3)

    def test_most_rented_movies(self):
        # r1 = Rental(90, 106 , 10, None, None, None)
        # r2 = Rental(91, 100, 11)
        # r3 = Rental(92, 106, 12)
        # self.rentalsList.add(r1)
        # self.rentalsList.add(r2)
        # self.rentalsList.add(r3)
        self.assertEqual(len(self.rentalsList.most_rented_movies()), 2)
        self.assertEqual(self.rentalsList.most_rented_movies()[0][0], 106 )
    def test_late_returns(self):
        self.assertEqual(len(self.rentalsList.late_returns()), 0)
    def test_late_returns_2(self):
        self.rentalsList._return(0)
        self.assertEqual(len(self.rentalsList.late_returns()), 1)
    def tearDown(self):
        pass


#class