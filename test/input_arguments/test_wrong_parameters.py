import unittest

from src.exceptions.exceptions import InvalidArgumentException
from src.domain.fitters.fitter import Fitter


class TestWrongParameters(unittest.TestCase):

    def test_wrong_project_name(self):
        with self.assertRaises(InvalidArgumentException) as error:
            Fitter().fit('goel-okumoto', 'waterfall-x')
        self.assertEqual(error.exception.strerror, 'The requested project is not on the repository')

    def test_wrong_model(self):
        with self.assertRaises(InvalidArgumentException) as error:
            Fitter().fit('hiroshima-nagasaki', 'ntds')
        self.assertEqual(error.exception.strerror, 'The requested model does not exist')
