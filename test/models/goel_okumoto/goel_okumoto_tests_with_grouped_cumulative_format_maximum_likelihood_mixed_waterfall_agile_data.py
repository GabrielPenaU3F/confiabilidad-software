import unittest

from src.fitters.fitter import GroupedCumulativeFitter


class GoelOkumotoTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = GroupedCumulativeFitter().fit('goel-okumoto', 'mixed-waterfall-agile')

    def test_mixed_waterfall_agile_goel_okumoto_maximum_likelihood_a_parameter_is_1755_comma_604133(self):
        a = GoelOkumotoTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1755.604133, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_maximum_likelihood_b_parameter_is_0_comma_003567(self):
        b = GoelOkumotoTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.003567, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_maximum_likelihood_prr_is_9_comma_721876(self):
        prr = GoelOkumotoTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 9.721876, places=6)

    def test_mixed_waterfall_agile_goel_okumoto_aic_is_minus_746_comma_010244(self):
        aic = GoelOkumotoTestsWithGroupedCumulativeFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, -746.010244, places=6)
