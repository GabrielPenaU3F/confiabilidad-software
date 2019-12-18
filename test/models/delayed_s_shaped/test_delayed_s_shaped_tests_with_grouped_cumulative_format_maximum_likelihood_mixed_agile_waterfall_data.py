import unittest

from src.domain.fitters.fitter import GroupedCumulativeFitter


class DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', initial_approx=(1, 0.5))

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_a_parameter_is_862_comma_961708(self):
        a = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 862.961708, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_023332(self):
        b = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.023332, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_prr_is_1926_comma_376474(self):
        prr = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1926.376474, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_aic_is_minus_1450_comma_967420(self):
        aic = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1450.967420, places=6)
