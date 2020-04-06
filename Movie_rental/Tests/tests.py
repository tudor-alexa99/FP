import unittest
from repository.movies_repo import Movie_Repository
from domain.movie import Movie

class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        repo = Movie_Repository()
        movie = Movie(12, "Titanic", "Long", "Romance")
        repo.add(movie)
        repo.remove(12)
    def test_remove_movieId(self, repo):
        #self.setUp()
        # print(repo.getAll())
         #repo.add(movie)
        # print(repo.getAll())
        #repo.remove(12)
        self.assertEqual(len(repo.getAll() , 0))

    def test_add_movie(self):
        repo2 = Movie_Repository()
        new_movie = Movie(123, "Abc", "desc", "genre")
        repo2.add(new_movie)
        #print(repo2)
        self.assertEqual(len(repo2), 1)
    def tearDown(self):
        unittest.TestCase.tearDown(self)


run = Tests()
