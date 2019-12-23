import unittest

from src.domain.fitters.fitter import Fitter


class BarrazaContagionTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('barraza-contagion', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_barraza_contagion_least_squares_a_parameter_is_21_comma_042357(self):
        a = BarrazaContagionTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 21.042357, places=6)

    def test_mixed_waterfall_agile_barraza_contagion_least_squares_b_parameter_is_0_comma_786906(self):
        b = BarrazaContagionTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.786906, places=6)

    def test_mixed_waterfall_agile_barraza_contagion_least_squares_prr_is_7_comma_700165(self):
        prr = BarrazaContagionTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 7.700165, places=6)
