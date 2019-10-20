import unittest

from src.auxiliar_math import gamma


class TestLowerIncompleteGamma(unittest.TestCase):

    def test_lower_incomplete_gamma_1_2_is_0_comma_264241(self):
        self.assertAlmostEqual(0.264241, gamma.lower_incomplete_gamma(1, 2), places=6)

    def test_lower_incomplete_gamma_5_4_is_4_comma_41(self):
        self.assertAlmostEqual(4.41, gamma.lower_incomplete_gamma(5, 4), places=2)
