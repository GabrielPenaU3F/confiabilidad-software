import unittest

from src.fitters.fitter import TTFFitter


class GoelOkumotoTestsWithNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('goel-okumoto', 'ntds')

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_is_33_comma_99(self):
        a = GoelOkumotoTestsWithNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.993503, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_is_0_comma_0057(self):
        b = GoelOkumotoTestsWithNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.005790, places=6)

    def test_ntds_goel_okumoto_least_squares_a_parameter_is_33_comma_59(self):
        a = GoelOkumotoTestsWithNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 33.599359, places=6)

    def test_ntds_goel_okumoto_least_squares_b_parameter_is_0_comma_0062(self):
        b = GoelOkumotoTestsWithNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.006296, places=6)
