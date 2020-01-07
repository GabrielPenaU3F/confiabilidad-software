import unittest

from src.domain.fitters.model_fitter import ModelFitter


class MusaOkumotoTestsWithLeastSquaresMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('musa-okumoto', 'mixed-waterfall-agile', initial_approx=(1, 0.5), lsq_only=True)

    def test_mixed_waterfall_agile_musa_okumoto_least_squares_a_parameter_is_1006_comma_374788(self):
        a = MusaOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 1006.374788, places=6)

    def test_mixed_waterfall_agile_musa_okumoto_least_squares_b_parameter_is_0_comma_007034(self):
        b = MusaOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.007034, places=6)

    def test_mixed_waterfall_agile_musa_okumoto_least_squares_prr_is_9_comma_339123(self):
        prr = MusaOkumotoTestsWithLeastSquaresMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 9.339123, places=6)
