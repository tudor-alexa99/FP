from repository.clients_repo import Clients_Repository
from domain.client import Client

class TextfileClientsRepo(Clients_Repository):
    def __init__(self, file_name = 'repository/clients.txt'):
        Clients_Repository.__init__(self)
        self.file_name = file_name
        self._load_file()

    def add(self, new_client):
        Clients_Repository.add(self, new_client)
        self._save_file()

    def remove(self, pos):
        Clients_Repository.remove(self, pos)
        self._save_file()

    def delete_id(self, id):
        Clients_Repository.delete_id(self, id)
        self._save_file()

    #asa si cu Update si Delete/ Remove

    def _load_file(self):
        try:
            f = open(self.file_name, 'r')

            line = f.readline()
            while line != '':
                tok = line.split(",")
                client = Client(tok[0], int(tok[1]))
                Clients_Repository.add(self, client)
                line = f.readline()
        except IOError as e:
            raise Exception("cannot load file - " + str(e))
        finally:
            f.close()

    def _save_file(self):
        try:
            f = open(self.file_name, "w")

            for client in self.getAll():
                f.write(self._to_string(client) + "\n")
        except IOError as e:
            raise Exception("cannot write file - " + str(e))
        finally:
            f.close()

    def _to_string(self, client):
        return str(client.name) + "," +  str(client.id)