import unittest

from src.fitters.fitter import GroupedCumulativeFitter


class LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('logistic', 'mixed-waterfall-agile',
                                                initial_approx=(0.01, 0.001, 0.000001))

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_a_parameter_is_820_comma_450940(self):
        a = LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 820.450940, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_b_parameter_is_0_comma_041736(self):
        b = LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.041736, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_c_parameter_is_57_comma_488443(self):
        c = LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 57.488443, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_prr_is_11_comma_373068(self):
        prr = LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 11.373068, places=6)

    def test_mixed_waterfall_agile_logistic_aic_is_minus_1833_comma_933360(self):
        aic = LogisticTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1833.933360, places=6)
