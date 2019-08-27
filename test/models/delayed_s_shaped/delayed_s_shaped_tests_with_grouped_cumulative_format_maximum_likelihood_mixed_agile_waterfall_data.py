import unittest

from src.fitters.fitter import GroupedCumulativeFitter


class DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile')

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_a_parameter_is_862_comma_961708(self):
        a = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 862.961708, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_023332(self):
        b = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.023332, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_prr_is_1926_comma_376474(self):
        prr = DelayedSShapedTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1926.376474, places=6)

    ''' Not used test
    def test_mixed_waterfall_agile_delayed_s_shaped_aic_is_minus_746_comma_010244(self):
        aic = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, -746.010244, places=6)
    '''