import unittest

from src.domain.fitters.fitter import Fitter


class DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_a_parameter_is_976_comma_831477(self):
        a = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 976.831477, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_019047(self):
        b = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.019047, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_prr_is_3414_comma_616205(self):
        prr = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 3414.616205, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_aic_is_minus_1414_comma_986666(self):
        aic = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1414.986666, places=6)
