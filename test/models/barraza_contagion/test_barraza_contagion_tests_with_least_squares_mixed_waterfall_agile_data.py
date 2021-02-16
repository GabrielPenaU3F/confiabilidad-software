import unittest

from src.domain.fitters.model_fitter import ModelFitter


class BarrazaContagionTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('barraza-contagion', 'mixed-waterfall-agile', initial_approx=(1, 0.5),
                                    lsq_only=True, mts=False)

    def test_mixed_waterfall_agile_barraza_contagion_least_squares_a_parameter_is_21_comma_042428(self):
        a = self.__class__.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 21.042428, places=6)

    def test_mixed_waterfall_agile_barraza_contagion_least_squares_b_parameter_is_0_comma_786906(self):
        b = self.__class__.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.786906, places=6)

    def test_mixed_waterfall_agile_barraza_contagion_least_squares_prr_is_7_comma_708690(self):
        prr = self.__class__.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 7.708690, places=6)
