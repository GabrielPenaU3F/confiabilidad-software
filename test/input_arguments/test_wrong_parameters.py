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

    def test_wrong_initial_approx(self):
        with self.assertRaises(InvalidArgumentException) as error:
            Fitter().fit('goel-okumoto', 'ntds', initial_approx=('Wine', 'Beer'))
        self.assertEqual(error.exception.strerror, 'Initial approximation must be a real tuple or array')

    def test_decimal_end_sample(self):
        with self.assertRaises(InvalidArgumentException) as error:
            Fitter().fit('goel-okumoto', 'ntds', end_sample=5.66)
        self.assertEqual(error.exception.strerror, 'The end sample must be a positive integer')

    def test_negative_end_sample(self):
        with self.assertRaises(InvalidArgumentException) as error:
            Fitter().fit('goel-okumoto', 'ntds', end_sample=-2)
        self.assertEqual(error.exception.strerror, 'The end sample must be a positive integer')

    def test_negative_x0(self):
        with self.assertRaises(InvalidArgumentException) as error:
            Fitter().fit('goel-okumoto', 'ntds', x0=-2)
        self.assertEqual(error.exception.strerror, 'Initial condition x0 must be a positive number')
