import unittest

from domain.movie import Movie

class ValidateMovie:
    def validate(self, movie):
        _errors = []
        if isinstance(movie, Movie) == False:
            _errors.append("Instance error! The object 'movie' does not belong to the 'Movie' Class")

        if len(movie.title) == 0:
            _errors.append("The title should not be empty")

        if len((movie.descr)) == 0:
            _errors.append("The description should not be empty")

        if len((movie.genre)) == 0:
            _errors.append("The genre should not be empty")

        if len(_errors) != 0:
            raise ValueError(_errors)

        return True

class TestValidate(unittest.TestCase):
    def setUp(self):
        self.validator = ValidateMovie()

    def test_title(self):
        self.assertEqual(self.validator.validate(Movie(1, "T1", "D1", "G1")), True)
        self.assertRaises(ValueError, self.validator.validate, Movie(1, '', 'D1', 'G1'))

    def test_descr(self):
        self.assertEqual(self.validator.validate(Movie(1, "T1", "D1", "G1")), True)
        self.assertRaises(ValueError, self.validator.validate, Movie(1, 'T1', '', 'G1'))