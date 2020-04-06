from repository.rental_repo import Rental_Repository
import pickle


class BinaryRentalsRepo(Rental_Repository):
    def __init__(self, file_name='students.txt'):
        Rental_Repository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def store(self, obj):
        Rental_Repository._add(self, obj)
        self._store_file()

    def update(self, obj):
        pass
        #Rental_Repository.update(self, obj)
        #self._store_file()

    def delete(self, obj_id):
        Rental_Repository.remove_by_clientId(self, obj_id)
        self._store_file()

    def _load_file(self):
        f = open(self._file_name, 'rb')

        try:
            self._objects = pickle.load(f)
        except EOFError:
            self._objects = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def _store_file(self):
        f = open(self._file_name, 'wb')
        pickle.dump(self._objects, f)
        f.close()