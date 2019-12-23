import unittest

from src.domain.fitters.fitter import Fitter


class DelayedSShapedTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5), lsq_only=True)

    def test_mixed_waterfall_agile_delayed_s_shaped_least_squares_a_parameter_is_893_comma_638883(self):
        a = DelayedSShapedTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 893.638883, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_least_squares_b_parameter_is_0_comma_021788(self):
        b = DelayedSShapedTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.021788, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_least_squares_prr_is_2371_comma_329471(self):
        prr = DelayedSShapedTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2371.329471, places=6)
