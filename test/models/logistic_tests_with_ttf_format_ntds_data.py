import unittest

from src.fitters.fitter import TTFFitter


class LogisticTestsWithTTFFormatNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('logistic', 'ntds')

    def test_ntds_logistic_least_squares_a_parameter_is_24_comma_611413(self):
        a = LogisticTestsWithTTFFormatNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 24.611413, places=6)

    def test_ntds_logistic_least_squares_b_parameter_is_0_comma_041331(self):
        b = LogisticTestsWithTTFFormatNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.041331, places=6)

    def test_ntds_logistic_least_squares_c_parameter_is_76_comma_485839(self):
        c = LogisticTestsWithTTFFormatNtdsData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 76.485839, places=6)

    def test_ntds_logistic_maximum_likelihood_a_parameter_is_24_comma_611413(self):
        a = LogisticTestsWithTTFFormatNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.611413, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_is_0_comma_041331(self):
        b = LogisticTestsWithTTFFormatNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.041331, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_is_0_comma_485839(self):
        c = LogisticTestsWithTTFFormatNtdsData.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.485839, places=6)

    def test_ntds_logistic_least_squares_prr_is_0_comma_181087(self):
        prr = LogisticTestsWithTTFFormatNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 0.181087, places=6)

    def test_ntds_logistic_maximum_likelihood_prr_is_0_comma_181087(self):
        prr = LogisticTestsWithTTFFormatNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 0.181087, places=6)

    def test_ntds_logistic_aic_is_178_comma_515936(self):
        aic = LogisticTestsWithTTFFormatNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 178.515936, places=6)
