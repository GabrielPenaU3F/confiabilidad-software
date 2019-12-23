import unittest

from src.domain.fitters.fitter import Fitter


class GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('gompertz', 'mixed-waterfall-agile', initial_approx=(25, 0.5, 0.5))

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_a_parameter_is_1093_comma_671399(self):
        a = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1093.671399, delta=10**(-6))

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_b_parameter_is_0_comma_094026(self):
        b = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.094026, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_c_parameter_is_0_comma_985023(self):
        c = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 0.985023, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_prr_is_16_comma_974590(self):
        prr = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 16.974590, places=6)

    def test_mixed_waterfall_agile_gompertz_aic_is_1279_comma_818464(self):
        aic = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1279.818464, places=6)
