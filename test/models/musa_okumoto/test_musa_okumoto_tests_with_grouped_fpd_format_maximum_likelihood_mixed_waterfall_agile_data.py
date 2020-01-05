import unittest

from src.domain.fitters.model_fitter import ModelFitter


class MusaOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('musa-okumoto', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_musa_okumoto_maximum_likelihood_a_parameter_is_988_comma_847875(self):
        a = MusaOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 988.847876, places=6)

    def test_mixed_waterfall_agile_musa_okumoto_maximum_likelihood_b_parameter_is_0_comma_006937(self):
        b = MusaOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.006937, places=6)

    def test_mixed_waterfall_agile_musa_okumoto_maximum_likelihood_prr_is_9_comma_701588(self):
        prr = MusaOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 9.701588, places=6)

    def test_mixed_waterfall_agile_musa_okumoto_aic_is_1300_comma_538681(self):
        aic = MusaOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1300.538681, places=6)
