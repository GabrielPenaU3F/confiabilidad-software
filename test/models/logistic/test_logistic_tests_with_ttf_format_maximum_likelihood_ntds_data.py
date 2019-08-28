import unittest

from src.fitters.fitter import TTFFitter


class LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('logistic', 'ntds', initial_approx = (10, 0.05, 20))

    def test_ntds_logistic_maximum_likelihood_a_parameter_is_24_comma_611413(self):
        a = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.611413, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_is_0_comma_041331(self):
        b = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.041331, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_is_0_comma_485839(self):
        c = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.485839, places=6)

    def test_ntds_logistic_maximum_likelihood_prr_is_0_comma_181087(self):
        prr = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 0.181087, places=6)

    def test_ntds_logistic_aic_is_180_comma_515936(self):
        aic = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 180.515936, places=6)
