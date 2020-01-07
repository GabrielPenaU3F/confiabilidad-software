import unittest

from src.domain.fitters.model_fitter import ModelFitter


class BarrazaContagionTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('barraza-contagion', 'ntds', initial_approx=(1, 0.5))

    def test_ntds_barraza_contagion_least_squares_a_parameter_is_0_comma_379859(self):
        a = BarrazaContagionTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 0.379859, places=6)

    def test_ntds_barraza_contagion_least_squares_b_parameter_is_0_comma_645026(self):
        b = BarrazaContagionTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.645026, places=6)

    def test_ntds_barraza_contagion_least_squares_prr_is_1_comma_985367(self):
        prr = BarrazaContagionTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.985367, places=6)
