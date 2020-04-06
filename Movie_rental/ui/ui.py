from domain.movie import Movie
#from domain.client import Client
#from domain.rental import Rental
from iterable.iter import Iterable, shellSort
from repository.movies_repo import Movie_Repository
from repository.clients_repo import Clients_Repository
from repository.rental_repo import Rental_Repository
from datetime import datetime
from controller.client_controller import ClientController
#from domain.client_validator import Validate
#from statistics import *
from controller.movie_controller import MovieController
from controller.rental_controller import RentalController
#from statistics import _most_rented
#from ui.statistics import Statistics
from controller.undo_controller import UndoController
from repository.movies_repo import Movie_Repository
from repository.textfile_clients_repo import TextfileClientsRepo


class Ui:
    def __init__(self, undo_ctrl, rental_ctrl, client_ctrl, movie_ctrl):
        self.__undo_controller = undo_ctrl
        # settings = self.read_setting()
        # if settings["repo_type"] == "inmemory":
        #     self.__rental_repo = Rental_Repository()
        #     self.__movie_repo = Movie_Repository()
        #     self.__client_repo = Clients_Repository()

        self.__rental_controller = rental_ctrl
        self.__movie_controller = movie_ctrl
        self.__client_controller = client_ctrl
        # self.movie_iter = movies_iter
        # self.client_iter = client_iter
        # elif settings["repo_type"] == "text":
        #     #self.__rental_repo = TextfileRentalRepo
        #     #self.__movie_repo = TextfileMovieRepo()
        #     self.__client_repo = TextfileClientsRepo(settings["client_repo"])

        #elif settings["repo_type"] == "binary":
            #self.__rental_repo = BinaryfileRentalRepo
            #self.__movie_repo = BinaryfileMovieRepo()
            #self.__client_repo = BinaryfileClientsRepo()

    def read_setting(self):
        f = open("settings.properties", "r")
        s = f.read()
        lines = s.split("\n")

        settings = {}
        for line in lines:
            keyvalue = line.split("=")
            settings[keyvalue[0].strip()] = keyvalue[1].strip()

        return settings

    def printMenu(self):
        print("Choose submenu")
        print("1.Movies")
        print("2.Clients")
        print("3.Rentals")
        print("4.Search")
        print("5.Statistics")
        print("6.Undo")
        print("7.Redo")
        print("8.Sort")
        print("0.exit")

    def printSubmenuClients(self):
        """
        Divide the menu in multiple sub-menus, for each of the categories
        """
        print("1.Add client")
        print("2.Remove client")
        print("3.List clients")
        print("4.Update client")

    def printSubmenuMovies(self):
        print("1.Add movie")
        print("2.Remove movie")
        print("3.List movies")
        print("4.Update movie")

    def printSubmenuRental(self):
        print("1.Rent movie:")
        print("2.Return movie:")
        print("3.List all rentals:")

    def movie_addUI(self):
        try:
            id_ = int(input("id: "))
            if self.__movie_controller.find_by_id(id_) == True:
                print("\nThis id is already in use\n")
                return
        except ValueError:
            print("Please insert a number")

        try:
            title = input("Title:")
            genre = input("Genre:")
            descr = input("description: ")
            self.__movie_controller.add(id_,title, descr, genre)
            print("Movie added successfully")
        except ValueError as error:
            print(error)

    def client_addUI(self):
        try:
            _id = int(input("id: "))
            name = input("name: ")
            self.__client_controller.create(_id, name)
        except ValueError:
            print("the id has to be a number!")
        except NameError:
            print("The id is already in use")


    # def remove_movieId(self, movie_repo, id):
    #     # pass
    #     # remove the movies by id
    #     for mov in movie_repo:
    #         if mov.get_id() == id:
    #             movie_repo.pop(mov)
    #
    # def remove_client(self, client_repo, id):
    #     # remove the clients by id
    #     for client in client_repo:
    #         if client.get_id() == id:
    #             client_repo.pop(client)

    def listMovies(self, movie_repo):
        print(self.__movie_controller.getAll())

    def listClients(self, client_repo):
        print(self.__client_controller.getAll())


    def commandMenu(self):
        #self.__movie_repo.initialise()
        c = -1
        while c != 0:
            self.printMenu()
            c = input("Command: ")
            if c == "1":
                self.printSubmenuMovies()
                self.movieCommands()
            elif c == "2":
                self.printSubmenuClients()
                self.clientsCommands()
            elif c == "3":
                self.printSubmenuRental()
                self.rentalCommands()
            elif c == "4":
                self.search_something()
            elif c == "5":
                self.printStatisticsCommand()
                self.statistics()
            elif c == "6":
                self.__undo_controller.undo()
            elif c == "7":
                self.__undo_controller.redo()
            elif c == "8":
                # props = input("What criteria?: ")
                # self.__client_controller.shellSort(self.__client_controller.getAll, props)
                print("Choose list to sort: ")
                print("1.Movies")
                print("2.Clients")
                #print("3.Rentals")
                i = input(">")
                if i == "1":
                    #self.__client_controller.
                    #let = input ("Sort by a letter: ")
                    #self.movie_iter.shellSort()
                    #self.__movie_controller.shellSort(self.__movie_controller.iter.iter.iter.find_by_id(1))
                    movies = self.__movie_controller.getAll
                    print(movies)
                    shellSort(movies)
            elif c == "0":
                return
            else:
                print("Invalid command")


    def statistics(self):
        com = input("Choose a command from 1 to 4: ")
        if com == "1":
            print(self.__rental_controller.most_rented_movies())
        elif com == "2":
            print(self.__rental_controller.most_active_clients())
        elif com == "3":
            self.__rental_controller.list_rentals()
        elif com == "4":
            print(self.__rental_controller.late_returns())

    def printAllMovies(self):
        movieList = self.__movie_controller.getAll()
        for i in movieList:
            print(i)

    def printClientList(self):
        print("\t Clients list: \n")
        clientsList = self.__client_controller.getAll()
        for i in clientsList:
            print(i)

    def movieCommands(self):
        #self.__movie_controller.initialise()
        com = input("Please insert a number from 1 to 4: ")
        if com == "1":
            self.movie_addUI()

        if com == "2":
            self.printAllMovies()
            id = int(input("Please insert a valid movie id"))
            self.movie_remove(id)
        if com == "3":
            self.printAllMovies()
        if com == "4":
            self.printAllMovies()
            try:
                id = int(input("Please insert a valid movie id"))
            except ValueError:
                print("The id has to be a number")
                return
            self.updateMovie(id)

    def movie_remove(self, id):
        self.__movie_controller.remove(id)

    def updateMovie(self, id):
        try:
            if self.__movie_controller.find_by_id(id) == True:
                title = input("Title:")
                genre = input("Genre:")
                descr = input("description: ")
                self.__movie_controller.update(id, title,descr, genre)
                print("Movie updated successfully! ")
            else:
                print("The movie could not be found by this id!")
        except ValueError as error:
            print(error)
    def clientsCommands(self):
        com = input("Please insert a number from 1 to 4: ")
        if com == "1":
            self.client_addUI()
        if com == "2":
            id = int(input("Please insert a valid client id"))
            if self.__client_controller.find_by_id(id) == False:
                print("Unexisting client id")
            else:
                self.__client_controller.remove(id)
        if com == "3":
            self.printClientList()
        if com == "4":
            self.printClientList()
            id = int(input("Please insert a valid client id:"))
            if self.__client_controller.find_by_id(id) == False:
                print("Invalid id")
            else:
                name = input("Insert a new name here:")
                self.__client_controller.update(id, name)

    def client_remove(self, id):
        self.__client_controller.remove(id)

    #def printAllClients(self):
    #    clientList

    # def updateClient(self, id):
    #     name = input("Insert a new name here:")
    #     self.__client_repo.update(id, name)


    def rentalCommands(self):
        com = input("Choose a command from 1 to 3:")
        #self.__rental_repo.initialize()
        self.printSubmenuRental()
        if com == "1":
            self.rent_movie()
        elif com == "2":
            self.return_movie()
        elif com == "3":
            self.__rental_controller.list_rentals()

    def rent_movie(self):
        self.printAllMovies()
        self.printClientList()
        new_rent_id = self.__rental_controller.last_id()
        # fa-l controller

        # if self.__rental_repo.find_by_id(id) == False:
        #     print("Please insert an existing client id!\n")
        #     return
        try:
            movieId = int(input("Insert a movie's id here: "))

            #checks if the movie is in the movie list
            if self.__movie_controller.find_by_id(movieId) == False:
                print("\nPlease insert an existing movie id here!\n")
                return

            #checks if the movie has not been rented or if it was returned
            if self.__rental_controller.check_available_movie(movieId) == False:
                print("The movie is not available")
                return

            #checks if the client is in the clients list
            clientId = int(input("Insert a client id here: "))
            if self.__client_controller.find_by_id(clientId) == False:
                print("\nPlease insert an existing client id!\n")
                return
            days = int(input("How many days would you like to rent the movie?(between 0 and 100) :"))
            if days < 0 or days > 100:
                print("\nInvalid number")
                return
            if self.__rental_controller.check_valid_client(clientId) == True:
                self.__rental_controller.rent(new_rent_id, clientId, movieId, days, self.__client_controller, self.__movie_controller)

            else:
                print("This client has not returned a movie yet!")
        except ValueError:
            print("\nPlease insert a number")

    def return_movie(self):
        self.__rental_controller.list_rentals()
        try:
            id = int(input("Please insert a rental id here: "))
            position = self.__rental_controller.find_by_id(id)
            if position == False:
                print("Please insert a valid rental id here!")
                return
            if self.__rental_controller[position].due_date < datetime.now():
                print("\nYou have been late with your return!\n")
            self.__rental_controller._return(position)
        except ValueError:
            print("Please insert a number")

    def search_something(self):
        #self.__movie_repo.initialise()
        s_list = []
        com = input("Search for: ")
        for word in self.__client_controller.toString():
            if com.lower() in word.lower():
                s_list.append(word)
        for word in self.__movie_controller.toString():
            if com.lower() in word.lower():
                s_list.append(word)
        print(s_list)

    def printStatisticsCommand(self):
        print("\n 1. Most rented movies ")
        print("\n 2. Most active clients ")
        print("\n 3. List all rentals ")
        print("\n 4. The movies that were returned late")


# ui = Ui()
# ui.commandMenu()


# ui.printAllMovies()
# ui.printClientList()




import unittest

class Test_UI(unittest.TestCase):
    pass
    def setUp(self):
        self.repo = Movie_Repository()
    def test_remove_movieId(self):
        movie = Movie(12, "Titanic", "Long", "Romance")
        self.repo.add(movie)
        self.repo.remove(12)
        self.assertEqual(len(self.repo.getAll()), 0)


def check():
    rents = Rental_Repository()
    controller = RentalController(rents, True)
    print(controller.getAll())
    print(rents.getAll())

#check()
#test_remove_movieId()

#iuliana@cs.ubbcluj.ro