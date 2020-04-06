from domain import client_validator, movie_validator
from iterable.iter import Iterable
from repository.binaryfile_clients_repo import BinaryClientsRepo
from repository.binaryfile_movies_repo import BinaryMoviesRepo
from repository.binaryfile_rental_repo import BinaryRentalsRepo
from repository.textfile_movies_repo import TextfileMoviesRepo
from repository.textfile_rentals_repo import TextfileRentalsRepo
from ui.ui import Ui
from domain.movie import Movie
#from domain.client import Client
#from domain.rental import Rental
from repository.movies_repo import Movie_Repository
from repository.clients_repo import Clients_Repository
from repository.rental_repo import Rental_Repository
from datetime import datetime
from controller.client_controller import ClientController
#from domain.client_validator import Validate
#from statistics import *
from controller.movie_controller import MovieController
from controller.rental_controller import RentalController
#from statistics import _most_rented
#from ui.statistics import Statistics
from controller.undo_controller import UndoController
from repository.movies_repo import Movie_Repository
from repository.textfile_clients_repo import TextfileClientsRepo

def read_settings():
    f = open('settings.properties', 'r')
    s = f.read()
    lines = s.split('\n')

    settings = {}
    for line in lines:
        keyvalue = line.split('=')
        settings[keyvalue[0].strip()] = keyvalue[1].strip()

    return settings

def start():

    settings = read_settings()
    initialise = False
    if settings['repo_type'] == 'text':
        clients_repo = TextfileClientsRepo(settings['client_repo'])
        movies_repo = TextfileMoviesRepo(settings['movie_repo'])
        rentals_repo = TextfileRentalsRepo(settings['rental_repo'])
    elif settings['repo_type'] == 'binary':
        clients_repo = BinaryClientsRepo(settings['clients_binary'])
        movies_repo = BinaryMoviesRepo(settings['movies_binary'])
        rentals_repo = BinaryRentalsRepo(settings['rentals_binary'])
    else:
        #iter1 = Iterable()
        #iter2 = Iterable()
        clients_repo = Clients_Repository()
        movies_repo = Movie_Repository()
        rentals_repo = Rental_Repository()
        initialise = True

    clients_validator = client_validator.ValidateClient()
    movies_validator = movie_validator.ValidateMovie()

    undo_controller = UndoController()
    rental_controller = RentalController(rentals_repo, undo_controller, initialise)
    client_controller = ClientController(undo_controller, clients_repo, rentals_repo, initialise)
    movie_controller = MovieController(undo_controller, movies_repo, rentals_repo, initialise)

    ui = Ui(undo_controller, rental_controller, client_controller, movie_controller)
    ui.commandMenu()

# try:
start()             # Use this for usual start
# except Exception as e:
#     print(e)

