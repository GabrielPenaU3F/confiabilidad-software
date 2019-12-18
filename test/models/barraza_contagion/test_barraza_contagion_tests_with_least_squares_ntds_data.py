import unittest

from src.domain.fitters.fitter import TTFFitter


class BarrazaContagionTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('barraza-contagion', 'ntds', initial_approx=(1, 0.5))

    def test_ntds_barraza_contagion_least_squares_a_parameter_is_0_comma_379868(self):
        a = BarrazaContagionTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 0.379868, places=6)

    def test_ntds_barraza_contagion_least_squares_b_parameter_is_0_comma_645020(self):
        b = BarrazaContagionTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.645020, places=6)

    def test_ntds_barraza_contagion_least_squares_prr_is_1_comma_985390(self):
        prr = BarrazaContagionTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.985390, places=6)
