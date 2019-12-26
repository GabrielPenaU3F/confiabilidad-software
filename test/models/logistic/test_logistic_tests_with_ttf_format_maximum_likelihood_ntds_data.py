import unittest

from src.domain.fitters.model_fitter import ModelFitter


class LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('logistic', 'ntds', initial_approx=(10, 0.05, 20))

    def test_ntds_logistic_maximum_likelihood_a_parameter_is_24_comma_640875(self):
        a = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.640875, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_is_0_comma_041331(self):
        b = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.040930, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_is_0_comma_485839(self):
        c = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.510170, places=6)

    def test_ntds_logistic_maximum_likelihood_prr_is_0_comma_181087(self):
        prr = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 0.193478, places=6)

    def test_ntds_logistic_aic_is_180_comma_515936(self):
        aic = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 180.177299, places=6)
