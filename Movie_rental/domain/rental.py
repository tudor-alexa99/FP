class Rental:
    def __init__(self,  rentalID ,  movieId ,  clientId ,  rented_date = None, due_date = None,  returned_date = None ):
        self.__rentalId = rentalID
        self.__movieId = movieId
        self.__clientId = clientId
        self.__rented_date = rented_date
        self.__due_date = due_date
        self.__returned_date = returned_date
    @property
    def rentalId(self):
        return self.__rentalId

    @property
    def movieId(self):
        return self.__movieId

    @property
    def clientId(self):
        return self.__clientId

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def returned_date(self):
        return self.__returned_date

    def set_rentalId(self, new_val):
        self.__rentalId = new_val
    def set_movieId(self,new_val):
        self.__movieId = new_val
    def set_clientId(self ,new_val):
        self.__clientId = new_val
    def set_rented_date(self,new_val):
        self.__rented_date = new_val
    def set_due_date(self,new_val):
        self.__due_date = new_val
    def set_returned_date(self,new_val):
        self.__returned_date = new_val


    def __str__(self):
        return "Rental ID: " + str(self.__rentalId)+ "||    Movie ID: " + str(self.__movieId)+ "||    Client ID" + str(self.__clientId)+ "||    Rented date:" + str(self.__rented_date)+ "||    Due date:" + str(self.__due_date)+"||    Returned date: " + str(self.__returned_date) + "\n"
        #afisEAZA-LE FRUMOS
