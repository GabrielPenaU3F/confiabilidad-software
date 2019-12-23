import unittest

from src.domain.fitters.fitter import Fitter


class GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('gompertz', 'mixed-waterfall-agile', initial_approx=(25, 0.5, 0.5))

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_a_parameter_is_1094_comma_355072(self):
        a = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1094.355072, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_b_parameter_is_0_comma_094405(self):
        b = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.094405, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_c_parameter_is_0_comma_985037(self):
        c = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 0.985037, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_prr_is_17_comma_064811(self):
        prr = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 17.064812, places=6)

    def test_mixed_waterfall_agile_gompertz_aic_is_1279_comma_756365(self):
        aic = GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData.fit.get_aic()
        self.assertAlmostEqual(aic, 1279.756365, places=6)
