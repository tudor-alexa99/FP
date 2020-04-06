from repository.clients_repo import Clients_Repository
import pickle

class BinaryClientsRepo(Clients_Repository):
    def __init__(self, file_name = "clients_binary.txt"):
        Clients_Repository.__init__(self)
        self._file_name = file_name
        self._load_file()

    def add(self, new_client):
        Clients_Repository.add(self, new_client)
        self._store_file()

    def remove(self, pos):
        Clients_Repository.remove(self,pos)
        self._store_file()

    def _load_file(self):
        f = open(self._file_name, 'rb')

        try:
            self._clientList = pickle.load(f)
        except EOFError:
            self._clientList = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def _store_file(self):
        f = open(self._file_name, "wb")
        pickle.dump(self._clientList, f)
        f.close()
