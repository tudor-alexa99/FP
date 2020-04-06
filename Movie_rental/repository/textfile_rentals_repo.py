from datetime import date

from domain.movie import Movie
from domain.rental import Rental
from repository.movies_repo import Movie_Repository
from domain.client import Client
from repository.rental_repo import Rental_Repository


class TextfileRentalsRepo(Rental_Repository):
    def __init__(self, file_name = 'repository/rentals.txt'):
        Rental_Repository.__init__(self)
        self.file_name = file_name
        self._load_file()

    def _add(self, new_rental):
        Rental_Repository._add(self, new_rental)
        self._save_file()

    def remove(self, pos):
        Rental_Repository.remove(self, pos)
        self._save_file()

    def _load_file(self):
        try:
            f = open(self.file_name, 'r')

            line = f.readline()
            while line != '':
                tok = line.split(",")
                rented_date = tok[3].split('-')
                rent_year = rented_date[0]
                rent_month = rented_date[1]
                rent_day = rented_date[2]

                rented_date = date(int(rent_year), int(rent_month), int(rent_day))

                due_date = tok[4].split('-')
                due_year = due_date[0]
                due_month = due_date[1]
                due_day = due_date[2]

                due_date = date(int(due_year), int(due_month), int(due_day))

                if tok[5] == "None":
                    rental = Rental(int(tok[0]), int(tok[1]), int(tok[2]), rented_date, due_date, tok[5])
                else:
                    returned_date = tok[4].split('-')
                    returned_year = returned_date[0]
                    returned_month = returned_date[1]
                    returned_day = returned_date[2]

                    returned_date = date(int(returned_year), int(returned_month), int(returned_day))
                    rental = Rental(int(tok[0]), int(tok[1]), int(tok[2]), rented_date, due_date, returned_date)

                Rental_Repository._add(self, rental)
                line = f.readline()
        except IOError as e:
            raise Exception("cannot load file - " + str(e))
        finally:
            f.close()

    def _save_file(self):
        try:
            f = open(self.file_name, "w")

            for rental in self.getAll():
                f.write(self._to_string(rental) + "\n")
        except IOError as e:
            raise Exception("cannot write file - " + str(e))
        finally:
            f.close()

    def _to_string(self, rental):
        if rental.returned_date != None:
            return str(rental.rentalId) + "," +  str(rental.movieId) + ',' + str(rental.clientId) + ',' + str(rental.rented_date) + ',' + str(rental.due_date) + ',' + str(rental.returned_date)
        else:
            return str(rental.rentalId) + "," +  str(rental.movieId) + ',' + str(rental.clientId) + ',' + str(rental.rented_date) + ',' + str(rental.due_date) + ',' + "None"