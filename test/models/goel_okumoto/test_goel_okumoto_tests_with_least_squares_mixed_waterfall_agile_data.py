import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('goel-okumoto', 'mixed-waterfall-agile', initial_approx=(1, 0.5), lsq_only=True)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_a_parameter_is_1416_comma_915295(self):
        a = GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 1416.915295, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_b_parameter_is_0_comma_004807(self):
        b = GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.004807, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_least_squares_prr_is_9_comma_602625(self):
        prr = GoelOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 9.602625, places=6)
