import unittest

from src.fitters.fitter import GroupedFPDFitter


class GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedFPDFitter().fit('goel-okumoto', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_a_parameter_is_1416_comma_913890(self):
        a = GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 1416.913890, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_b_parameter_is_0_comma_004806(self):
        b = GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.004807, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_prr_is_9_comma_015730(self):
        prr = GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 9.015730, places=6)
