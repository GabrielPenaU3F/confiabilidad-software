import unittest

from src.fitters.fitter import TTFFitter


class GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5))

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_is_33_comma_993503(self):
        a = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.993503, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_is_0_comma_005790(self):
        b = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.005790, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_prr_is_1_comma_405048(self):
        prr = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1.405048, places=6)

    def test_ntds_goel_okumoto_aic_is_169_comma_380301(self):
        aic = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 169.380301, places=6)

    def test_ntds_goel_okumoto_mttf_for_k_equal_1_is_5_comma_2(self):
        mttf = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(1)
        self.assertAlmostEqual(mttf, 5.2, delta=0.1)

    def test_ntds_goel_okumoto_mttf_for_k_equal_2_is_10_comma_6(self):
        mttf = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(2)
        self.assertAlmostEqual(mttf, 10.6, delta=0.1)

    def test_ntds_goel_okumoto_mttf_for_k_equal_3_is_16_comma_2(self):
        mttf = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(3)
        self.assertAlmostEqual(mttf, 16.2, delta=0.1)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_1_is_5_comma_2(self):
        mtbf = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 5.2, delta=0.1)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_5_is_5_comma_9(self):
        mtbf = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.9, delta=0.1)

    def test_ntds_goel_okumoto_mtbf_for_k_equal_20_is_13_comma_7(self):
        mtbf = GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 13.7, delta=0.1)
