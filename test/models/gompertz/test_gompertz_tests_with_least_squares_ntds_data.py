import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GompertzTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('gompertz', 'ntds', initial_approx=(25, 0.5, 0.9), lsq_only=True)

    def test_ntds_gompertz_least_squares_a_parameter_is_25_comma_344149(self):
        a = GompertzTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 25.344149, places=6)

    def test_ntds_gompertz_least_squares_b_parameter_is_0_comma_006605(self):
        b = GompertzTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.006605, places=6)

    def test_ntds_gompertz_least_squares_c_parameter_is_0_comma_974335(self):
        c = GompertzTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 0.974335, places=6)

    def test_ntds_gompertz_least_squares_prr_is_1_comma_496248(self):
        prr = GompertzTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.496248, places=6)
