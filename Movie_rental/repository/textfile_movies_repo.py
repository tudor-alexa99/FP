from domain.movie import Movie
from repository.movies_repo import Movie_Repository
from domain.client import Client

class TextfileMoviesRepo(Movie_Repository):
    def __init__(self, file_name = 'repository/clients.txt'):
        Movie_Repository.__init__(self)
        self.file_name = file_name
        self._load_file()

    def add(self, new_client):
        Movie_Repository.add(self, new_client)
        self._save_file()

    def remove(self, pos):
        Movie_Repository.remove(self, pos)
        self._save_file()


    #asa si cu Update si Delete/ Remove

    def _load_file(self):
        try:
            f = open(self.file_name, 'r')

            line = f.readline()
            while line != '':
                tok = line.split(",")
                movie = Movie(int(tok[0]), tok[1], tok[2], tok[3])
                Movie_Repository.add(self, movie)
                line = f.readline()
        except IOError as e:
            raise Exception("cannot load file - " + str(e))
        finally:
            f.close()

    def _save_file(self):
        try:
            f = open(self.file_name, "w")

            for movie in self.getAll():
                f.write(self._to_string(movie) + "\n")
        except IOError as e:
            raise Exception("cannot write file - " + str(e))
        finally:
            f.close()

    def _to_string(self, movie):
        return str(movie.id) + "," +  str(movie.title) + ',' + movie.descr + ',' + movie.genre