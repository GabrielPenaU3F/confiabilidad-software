import unittest

from src.domain.fitters.fitter import Fitter


class GompertzTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('gompertz', 'ntds', initial_approx=(25, 0.5, 0.5), lsq_only=True)

    def test_ntds_gompertz_least_squares_a_parameter_is_25_comma_340913(self):
        a = GompertzTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 25.340913, places=6)

    def test_ntds_gompertz_least_squares_b_parameter_is_0_comma_006556(self):
        b = GompertzTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.006556, places=6)

    def test_ntds_gompertz_least_squares_c_parameter_is_0_comma_974313(self):
        c = GompertzTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 0.974313, places=6)

    def test_ntds_gompertz_least_squares_prr_is_1_comma_507181(self):
        prr = GompertzTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.525308, places=6)
