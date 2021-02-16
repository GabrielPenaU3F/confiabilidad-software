import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GompertzTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('gompertz', 'mixed-waterfall-agile', initial_approx=(25, 0.5, 0.5),
                                    lsq_only=True, mts=False)

    def test_mixed_waterfall_agile_gompertz_least_squares_a_parameter_is_885_comma_875925(self):
        a = self.__class__.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 885.875925, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_b_parameter_is_0_comma_040078(self):
        b = self.__class__.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.040078, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_c_parameter_is_0_comma_980456(self):
        c = self.__class__.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 0.980456, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_prr_is_2_comma_522043(self):
        prr = self.__class__.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2.987893, places=6)
