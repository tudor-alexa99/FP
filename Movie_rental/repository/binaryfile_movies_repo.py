from repository.movies_repo import Movie_Repository
import pickle

class BinaryMoviesRepo(Movie_Repository):
    def __init__(self, file_name = "movies_binary.txt"):
        Movie_Repository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def add(self, new_movie):
        Movie_Repository.add(self, new_movie)
        self._store_file()

    # def update(self, new_client):
    #     Clients_Repository.update(self, new_client)
    #     self._store_file()

    def remove(self, pos):
        Movie_Repository.remove(pos)
        self._store_file()

    #asa si cu Update si Delete/ Remove


    def _load_file(self):
        f = open(self._file_name, 'rb')

        try:
            self._movieList = pickle.load(f)
        except EOFError:
            self._movieList = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def _store_file(self):
        f = open(self._file_name, "wb")
        pickle.dump(self._movieList, f)
        f.close()
