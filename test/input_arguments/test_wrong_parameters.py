import unittest

from src.exceptions.exceptions import InvalidArgumentException
from src.fitters.fitter import TTFFitter


class TestWrongParameters(unittest.TestCase):

    def test_wrong_project_name(self):
        with self.assertRaises(InvalidArgumentException) as error:
            TTFFitter().fit('goel-okumoto', 'waterfall-x')
        self.assertEqual(error.exception.strerror, 'The requested project is not on the repository')

    def test_wrong_model(self):
        with self.assertRaises(InvalidArgumentException) as error:
            TTFFitter().fit('hiroshima-nagasaki', 'ntds')
        self.assertEqual(error.exception.strerror, 'The requested model does not exist')

    def test_wrong_fitter_for_project(self):
        with self.assertRaises(InvalidArgumentException) as error:
            TTFFitter().fit('logistic', 'mixed-waterfall-agile')
        self.assertEqual(error.exception.strerror, 'The fitter does not match the requested project\'s data format')
