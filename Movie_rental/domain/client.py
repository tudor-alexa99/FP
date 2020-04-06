class Client:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    @property
    def name(self):
        return  str(self.__name)

    @property
    def id(self):
        return  self.__id

    def set_name(self, new_name):
        self.__name = new_name

    def set_id(self, new_id):
        self.__id = new_id

    def __str__(self):
        return "Id: " + str(self.__id) + "  ||  Name: " + str(self.__name)

    def toString(self):
        return [str(self.id), self.name]
