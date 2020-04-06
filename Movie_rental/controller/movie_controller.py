from domain.movie import Movie
from domain.movie_validator import ValidateMovie
from repository.movies_repo import Movie_Repository
from controller.undo_controller import *
from repository.rental_repo import Rental_Repository

class MovieController:
    def __init__(self,undo_controller,movie_repo, rental_repo, setup = True):
        """
        Uses the setup = True in order to enable testing
        without the automatic initiation
        """
        self._movieList = movie_repo
        self._rentalsList = rental_repo
        self._validator = ValidateMovie()
        if setup == True:
            self.initialise()
        self._undoController = undo_controller

    def add(self, movieId, title, description, genre):
        """
        Takes all the parameters needed to create a new movie
        Creates a movie
        Validates it
        If the movie is valid, it is added to the list
        """
        movie = Movie(movieId,title,description,genre)
        self._validator.validate(movie)
        self._movieList.add(movie)
        undo = FunctionCall(self.remove, movieId)
        redo = FunctionCall(self.add, movieId, title, description, genre)
        operation = Operation(undo, redo)
        self._undoController.addOperation(operation)

    def initialise(self):
        self._movieList.add(Movie(100, "Titanic", "Lame", "Romance"))
        self._movieList.add(Movie(101, "Life Of Pi", "Kids stuff", "Something"))
        self._movieList.add(Movie(102, "F&F", "Boys stuff", "Action"))
        self._movieList.add(Movie(103, "Godzilla", "Description", "Fiction"))
        self._movieList.add(Movie(104, "Maze Runner", "Description", "Action"))
        self._movieList.add(Movie(105, "Silence of the lambs", "Description", "Thriller"))
        self._movieList.add(Movie(106, "Narcos", "descripiton", "Police"))
        self._movieList.add(Movie(107, "Batman", "descripiton", "Action"))
        self._movieList.add(Movie(108, "Dark knight", "descripiton", "Action"))
        self._movieList.add(Movie(109, "Inseption", "descripiton", "Drama"))
        self._movieList.add(Movie(110, "The 300", "descripiton", "History"))
        self._movieList.add(Movie(111, "Bones", "descripiton", "Police"))
        self._movieList.add(Movie(112, "Girl with the dragon tatoo", "descripiton", "Action"))
        self._movieList.add(Movie(113, "Tu piel", "descripiton", "Drama"))
        self._movieList.add(Movie(114, "Soy el mana", "descripiton", "Drama"))
        self._movieList.add(Movie(115, "No man's land", "descripiton", "Action"))
        self._movieList.add(Movie(116, "The sound", "descripiton", "Sci-FI"))
        self._movieList.add(Movie(117, "Down of the planet of the apes", "descripiton", "Action"))
        self._movieList.add(Movie(118, "The awakening", "descripiton", "Horros"))
        self._movieList.add(Movie(119, "The hobbit", "descripiton", "Action"))
        self._movieList.add(Movie(120, "Friends", "descripiton", "Commedy"))
        self._movieList.add(Movie(121, "Why him?", "descripiton", "Commendy"))
        self._movieList.add(Movie(122, "Beyond", "description", "Artistic"))
        self._movieList.add(Movie(123, "The Universe", "description", "Documentary"))
        self._movieList.add(Movie(124, "Narnia", "description", "Fantasy"))
        self._movieList.add(Movie(125, "Lord of the Rings", "description", "Fantasy"))
        self._movieList.add(Movie(126, "Baywatch", "description", "Comedy"))
        self._movieList.add(Movie(127, "GOT", "description", "Fantasy"))
        self._movieList.add(Movie(128, "2012-The end", "description", "Action"))
        self._movieList.add(Movie(129, "Sailor moon", "description", "Anime"))
        self._movieList.add(Movie(130, "Naruto", "description", "Anime"))
        self._movieList.add(Movie(131, "Boruto", "description", "Anime"))
        self._movieList.add(Movie(132, "Bleach", "description", "Anime"))
        self._movieList.add(Movie(133, "The lost Land", "description", "Animation"))
        self._movieList.add(Movie(134, "The lion King", "description", "Animation"))
        self._movieList.add(Movie(135, "Farcry", "description", "Games"))
        self._movieList.add(Movie(136, "Django", "description", "Adventure"))
        self._movieList.add(Movie(137, "Jumanji", "description", "Adventure"))
        self._movieList.add(Movie(138, "Sherlock Holmes", "description", "Detective"))
        self._movieList.add(Movie(139, "CSI", "description", "Police"))
        self._movieList.add(Movie(140, "Star wars", "description", "Sci-FI"))
        self._movieList.add(Movie(141, "Star Treck", "description", "Sci-FI"))
        self._movieList.add(Movie(142, "La La Land", "description", "Musical"))
        self._movieList.add(Movie(143, "Seinfield", "description", "Comedy"))
        self._movieList.add(Movie(144, "Garfield", "description", "Animation"))
        self._movieList.add(Movie(145, "Mickey Mouse Club", "description", "Animation"))
        self._movieList.add(Movie(146, "Bohemian Rhapsody", "description", "Documentary"))
        self._movieList.add(Movie(147, "Bad Luck", "description", "Comedy"))
        self._movieList.add(Movie(148, "The downfall", "description", "Action"))
        self._movieList.add(Movie(149, "Divergent", "description", "Action"))
        self._movieList.add(Movie(150, "The hunger games", "description", "Action"))



    def remove(self, id):
        '''
        Looks for the position in which the movie has the given id and deletes it
        '''
        co = CascadedOperation()
        pos = 0
        for movie in self._movieList:
            if movie.id == id:
                undo = FunctionCall(self.add, movie.id, movie.title, movie.descr, movie.genre)
                redo = FunctionCall(self.remove, movie.id)
                self._movieList.remove(pos)
                operation = Operation(undo, redo)
                #self._undoController.addOperation(operation)
                co.add(operation)
            pos += 1

        l = self._rentalsList.getAll()
        #print(self._rentalsList.getAll())
        for rent in l:
            if rent.movieId == id:
                undo = FunctionCall(self._rentalsList.create_rental, rent.rentalId, rent.movieId, rent.clientId, rent.rented_date, rent.due_date, rent.returned_date)
                redo = FunctionCall(self._rentalsList.remove_by_movieId, rent.movieId)
                oper = Operation(undo, redo)
                co.add(oper)
                self._undoController.addOperation(co)
                self._rentalsList.remove_by_movieId(rent.movieId)

    def update(self, id, title, descr, genre):
        """
        Takes all the needed parameters to update the movie
        with the given id
        If the new movie introduced is not valid, raises a NameError and does not update
        """
        test_movie = Movie(id, title,descr, genre)
        self._validator.validate(test_movie)
        for movie in self._movieList:
            if movie.id == id:
                movie.descr = descr
                movie.title = title
                movie.genre = genre

    def find_by_id(self, movieId):
        """"
       Checks is the movie with the given id is in the list
        """
        for movie in self._movieList:
            if movie.id == movieId:
                return True
        return False

    def get_position(self,id):
        """
        Searches for the position in which the movie with
        the given id is found
        """
        i = 0
        for movie in self._movieList:
            if movie.id == id:
                return i
            i += 1
    def toString(self):
        """
        Function used for the 'Search' instruction
        Takes all the elements of the list and return them as a list of strings
        """
        lst = []
        for movie in self._movieList:
            lst.extend(movie.to_String())
        return lst

    def getAll(self):
        return self._movieList.getAll()

    def __getitem__(self, item):
        return self._movieList[item]
    @property
    def iter(self):
        return self._movieList.iter

def check_this_out():
    control = MovieController(False)
    #m1 = Movie(100, "t1", "d1", "g1")
    control.add(100, "t1", "d1", "g1")
    control.add(101, "t2", "d2", "g2")
    control.add(102, "t3", "d3", "g3")
    print(control.toString())
    control._undoController.undo()
    print("\n", control.toString())
    control._undoController.redo()
    print("\n", control.toString())

#check_this_out()
