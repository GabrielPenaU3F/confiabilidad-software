import unittest

from src.fitters.fitter import GroupedFailuresPerDayFitter


class LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedFailuresPerDayFitter().fit('logistic', 'mixed-waterfall-agile',
                                                    initial_approx=(0.01, 0.001, 0.00001))

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_a_parameter_is_835_comma_522623(self):
        a = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 835.522623, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_b_parameter_is_0_comma_022889(self):
        b = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.022889, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_c_parameter_is_88_comma_952788(self):
        c = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 88.952788, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_prr_is_13_comma_919258(self):
        prr = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 13.919258, places=6)

    def test_mixed_waterfall_agile_logistic_aic_is_minus_1408_comma_129803(self):
        aic = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1408.129803, places=6)
