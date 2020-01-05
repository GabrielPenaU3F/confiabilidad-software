import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GoelOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('goel-okumoto', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_goel_okumoto_maximum_likelihood_a_parameter_is_1373_comma_290255(self):
        a = GoelOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1373.290255, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_maximum_likelihood_b_parameter_is_0_comma_004957(self):
        b = GoelOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.004957, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_maximum_likelihood_prr_is_9_comma_625285(self):
        prr = GoelOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 9.625285, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_aic_is_1291_comma_698465(self):
        aic = GoelOkumotoTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1291.698465, places=6)
