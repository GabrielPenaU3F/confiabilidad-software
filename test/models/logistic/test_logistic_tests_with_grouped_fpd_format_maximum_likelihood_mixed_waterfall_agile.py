import unittest

from src.domain.fitters.model_fitter import ModelFitter


class LogisticTestsWithGroupedFailuresPerDayFormatMaximumLikelihoodMixedWaterfallAgileData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('logistic', 'mixed-waterfall-agile', initial_approx=(800, 0.03, 75), mts=False)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_a_parameter_is_1173_comma_028352(self):
        a = self.__class__.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1173.028352, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_b_parameter_is_0_comma_017837(self):
        b = self.__class__.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.017837, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_c_parameter_is_92_comma_402002(self):
        c = self.__class__.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 92.402002, places=6)

    def test_mixed_waterfall_agile_logistic_maximum_likelihood_prr_is_23_comma_409380(self):
        prr = self.__class__.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 23.409380, places=6)

    def test_mixed_waterfall_agile_logistic_aic_is_1345_comma_752429(self):
        aic = self.__class__.fit.get_aic()
        self.assertAlmostEqual(aic, 1345.752429, places=6)
