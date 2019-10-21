import unittest

from src.fitters.fitter import TTFFitter


class LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('logistic', 'ntds', initial_approx=(10, 0.05, 20))

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
        
    def test_ntds_logistic_mttf_for_k_equal_1_is_5_comma_6(self):
        mttf = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(1)
        self.assertAlmostEqual(mttf, 5.6, delta=0.1)

    def test_ntds_logistic_mttf_for_k_equal_2_is_15_comma_4(self):
        mttf = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(2)
        self.assertAlmostEqual(mttf, 15.4, delta=0.1)

    def test_ntds_logistic_mttf_for_k_equal_3_is_25_comma_3(self):
        mttf = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(3)
        self.assertAlmostEqual(mttf, 25.3, delta=0.1)

    def test_ntds_logistic_mtbf_for_k_equal_1_is_5_comma_6(self):
        mtbf = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 5.6, delta=0.1)

    def test_ntds_logistic_mtbf_for_k_equal_5_is_7_comma_1(self):
        mtbf = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 7.1, delta=0.1)

    def test_ntds_logistic_mtbf_for_k_equal_20_is_4_comma_1(self):
        mtbf = LogisticTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 4.1, delta=0.1)
