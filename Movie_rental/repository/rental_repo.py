# from repository.clients_repo import Clients_Repository
# from repository.movies_repo import Movie_Repository
from domain.rental import Rental
from datetime import datetime


class Rental_Repository(object):
    def __init__(self):
        self.__rentalList = []
        #n is the number of days

    def _add(self, rental):
        self.__rentalList.append(rental)

    def remove(self, pos):
        self.__rentalList.pop(pos)

    def remove_by_clientId(self, clientID):
        pos = 0
        for rent in self.__rentalList:
            if rent.clientId == clientID:
                self.__rentalList.pop(pos)
            pos += 1
    def create_rental(self,  rentalID ,  movieId ,  clientId ,  rented_date = None, due_date = None,  returned_date = None ):
        rent = Rental( rentalID ,  movieId ,  clientId ,  rented_date, due_date ,  returned_date)
        self._add(rent)


    # def rent(self,rentalId, clientId, movieId, n):
    #     returned_date = None # None
    #     # fa-l input cu numarul de zile
    #     rented_date = datetime.now()
    #     due_date = datetime.now() + timedelta(days = n)
    #     print(clientId, movieId, self.__client_repo.get_position(clientId))
    #     if self.__client_repo.find_by_id(clientId) :
    #         if self.__movie_repo.find_by_id(movieId) == True:
    #             client = self.__client_repo[self.__client_repo.get_position(clientId)]
    #             movie = self.__movie_repo[self.__movie_repo.get_position(movieId)]
    #             print("The Client:", client.name, "rented the movie: ", movie.title, " ")
    #             rental = Rental(rentalId, movie.id, client.id, rented_date, due_date, returned_date)
    #             self.__rentalList.append(rental)

    # def find_by_id(self, id):
    #     i = 0
    #     found = 0
    #     for rent in self.__rentalList:
    #         if rent.rentalId == id:
    #             found = 1
    #             return i
    #         i += 1
    #     if found == 0:
    #         return False

    # def _return(self, pos):
    #     returned_date = datetime.now()
    #     self.__rentalList[pos].set_returned_date(returned_date)self.

    def getAll(self):
        return self.__rentalList


    # def check_valid_client(self, clientId):
    #     for rental in self.__rentalList:
    #         if rental.clientId == clientId and (rental.returned_date == None and rental.due_date < datetime.now()):
    #             return False
    #     return True

    def __getitem__(self, item):
        return self.__rentalList[item]

    # def last_id(self):
    #     if len(self.__rentalList) == 0:
    #         return 0
    #     else:
    #         return self.__rentalList[-1].rentalId + 1

    def size(self):
        return len(self.__rentalList)

    # def list_rentals(self):
    #     # for rent in self.__rentalList:
    #     #    print(rent, "\n")
    #     for i in range(0, len(self.__rentalList)):
    #         print(self.__rentalList[i])

    #def initialize(self):
        # r1 = Rental(1, 100, 10, datetime(2018, 3, 10), datetime(2018, 3, 20), None)
        # r2 = Rental(2, 101, 11, datetime(2018, 4, 12), datetime(2018,12, 20), None)
        # r3 = Rental(3, 102, 12, datetime(2018, 5, 12), datetime(2018,12, 20),datetime(2018, 10, 22))
        # r4 = Rental(4, 103, 12, datetime(2018, 10, 24), datetime(2018,11, 20),None)
        # self.__rentalList = [r1, r2, r3, r4]

    # def check_available_movie(self, id):
    #     for rental in self.__rentalList:
    #         if rental.movieId == id:
    #             if rental.returned_date == None:
    #                 return False
    #     return True
    def remove_by_movieId(self, movieId):
        pos = 0
        for rent in self.__rentalList:
            if rent.movieId == movieId:
                self.__rentalList.pop(pos)
            pos += 1

# def test_find_by_id():
#     lst = Rental_Repository([],[])
#     lst.initialize()
#     assert lst.find_by_id(1) == 0 ,"Something's wrong"
#     #print (lst.find_by_id(2))
#     assert lst.find_by_id(1000) == False , "Oops"

#test_find_by_id()