import unittest

from src.domain.fitters.fitter import Fitter


class DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_a_parameter_is_929_comma_753752(self):
        a = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 929.753752, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_023049(self):
        b = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.023049, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_prr_is_1733_comma_312768(self):
        prr = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1733.312768, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_aic_is_minus_1442_comma_000199(self):
        aic = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1442.000199, places=6)
