from domain.client import Client
from repository.clients_repo import Clients_Repository
class ValidateClient:
    def checkId(self, _id):
        if type(_id) != int:
            return False
        return True

    def validate(self, client):
        '''
        Checks whether the client is an instance of the Client class and
        if the id and name are introduces correctly
        '''
        if isinstance(client, Client) == False:
            raise TypeError ("The client does not belong to the proper class")
        _errors = []
        if self.checkId(client.id) == False:
            _errors.append("Invalid id")
        if len(client.name) == 0:
            _errors.append("Empty client name")
        #if find_by_id(client.id)
        if len(_errors) != 0:
            #return _errors
            raise ValueError(_errors)

