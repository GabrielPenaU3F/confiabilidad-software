import unittest

from src.fitters.fitter import GroupedCumulativeFitter


class DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile')

    def test_mixed_waterfall_agile_delayed_s_shaped_least_squares_a_parameter_is_893_comma_638883(self):
        a = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 893.638883, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_least_squares_b_parameter_is_0_comma_021788(self):
        b = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.021788, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_a_parameter_is_862_comma_961708(self):
        a = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 862.961708, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_023332(self):
        b = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.023332, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_least_squares_prr_is_2371_comma_329475(self):
        prr = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2371.329475, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_prr_is_1926_comma_376474(self):
        prr = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1926.376474, places=6)

    # Todo: corregir el bug con el lambda arrancando en cero
    ''' Still INF 
    def test_mixed_waterfall_agile_delayed_s_shaped_aic_is_minus_746_comma_010244(self):
        aic = DelayedSShapedTestsWithGroupedCumulativeFormatMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, -746.010244, places=6)
    '''