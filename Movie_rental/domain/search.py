from repository.movies_repo import Movie_Repository
from repository.clients_repo import Clients_Repository
class Search:
    def __init__(self, movie_repo, clients_repo, command):
        self.__movies = movie_repo
        self.__clinets = clients_repo
        self.__com = command

    def search(self):
        pass
        allstr = self.__movies.toString()
        return self.__movies.toString()

def testSearch():
    movies = Movie_Repository()
    clients = Clients_Repository()
    movies.initialise()
    #print(movies.toString())
    src = Search(movies, clients, "Titanic")
    print(src.search())

testSearch()