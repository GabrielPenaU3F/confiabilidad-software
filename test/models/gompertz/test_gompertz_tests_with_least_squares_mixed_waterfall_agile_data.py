import unittest

from src.domain.fitters.fitter import Fitter


class GompertzTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('gompertz', 'mixed-waterfall-agile', initial_approx=(25, 0.5, 0.5), lsq_only=True)

    def test_mixed_waterfall_agile_gompertz_least_squares_a_parameter_is_885_comma_133698(self):
        a = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 885.133698, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_b_parameter_is_0_comma_039689(self):
        b = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.039689, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_c_parameter_is_0_comma_980400(self):
        c = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 0.980400, places=6)

    def test_mixed_waterfall_agile_gompertz_least_squares_prr_is_2_comma_470130(self):
        prr = GompertzTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2.470130, places=6)
