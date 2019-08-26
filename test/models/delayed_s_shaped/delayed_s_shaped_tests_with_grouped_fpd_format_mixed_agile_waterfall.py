import unittest

from src.fitters.fitter import GroupedFailuresPerDayFitter


class DelayedSShapedTestsWithGroupedFailuresPerDayFormatMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedFailuresPerDayFitter().fit('delayed-s-shaped', 'mixed-waterfall-agile')

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_a_parameter_is_976_comma_831477(self):
        a = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 976.831477, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_019047(self):
        b = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.019047, places=6)

    def test_mixed_waterfall_agile_delayed_s_shaped_maximum_likelihood_prr_is_3414_comma_616205(self):
        prr = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 3414.616205, places=6)

    # Todo: corregir el bug con el lambda arrancando en cero
    ''' Still INF 
    def test_mixed_waterfall_agile_delayed_s_shaped_aic_is_minus_3414_comma_616205(self):
        aic = DelayedSShapedTestsWithGroupedFailuresPerDayFormatMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 3414.616205, places=6)
    '''
