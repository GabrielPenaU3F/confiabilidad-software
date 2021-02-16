import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GompertzTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('gompertz', 'mixed-waterfall-agile', initial_approx=(25, 0.5, 0.5), mts=False)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_a_parameter_is_1093_comma_757870(self):
        a = self.__class__.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1093.757870, delta=10**(-6))

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_b_parameter_is_0_comma_094074(self):
        b = self.__class__.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.094074, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_c_parameter_is_0_comma_985025(self):
        c = self.__class__.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 0.985025, places=6)

    def test_mixed_waterfall_agile_gompertz_maximum_likelihood_prr_is_17_comma_773591(self):
        prr = self.__class__.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 17.773591, places=6)

    def test_mixed_waterfall_agile_gompertz_aic_is_1279_comma_810573(self):
        aic = self.__class__.fit.get_aic()
        self.assertAlmostEqual(aic, 1279.810573, places=6)
