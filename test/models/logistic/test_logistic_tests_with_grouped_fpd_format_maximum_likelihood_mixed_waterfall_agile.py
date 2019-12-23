import unittest

from src.domain.fitters.fitter import Fitter


class LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('logistic', 'mixed-waterfall-agile', initial_approx=(800, 0.03, 75))

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_a_parameter_is_835_comma_482786(self):
        a = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 835.482786, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_b_parameter_is_0_comma_022953(self):
        b = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.022953, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_c_parameter_is_89_comma_594643(self):
        c = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 89.594643, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_prr_is_14_comma_067516(self):
        prr = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 14.067516, places=6)

    def test_mixed_waterfall_agile_logistic_aic_is_minus_1408_comma_129803(self):
        aic = LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1410.448006, places=6)
