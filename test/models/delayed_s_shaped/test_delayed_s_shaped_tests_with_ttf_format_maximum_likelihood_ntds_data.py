import unittest

from src.fitters.fitter import TTFFitter


class DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('delayed-s-shaped', 'ntds', initial_approx=(1, 0.5))

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_is_27_comma_491544(self):
        a = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.491544, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_018579(self):
        b = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.018579, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_prr_is_3_comma_990516(self):
        prr = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 3.990516, places=6)

    def test_ntds_delayed_s_shaped_aic_is_165_comma_835957(self):
        aic = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 165.835957, places=6)

    def test_mttf_for_k_equal_1_is_14_comma_4(self):
        mttf = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(1)
        self.assertAlmostEqual(mttf, 14.4, places=1)

    def test_mttf_for_k_equal_2_is_22_comma_6(self):
        mttf = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(2)
        self.assertAlmostEqual(mttf, 22.6, places=1)

    def test_mttf_for_k_equal_3_is_29_comma_3(self):
        mttf = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mttf(3)
        self.assertAlmostEqual(mttf, 29.3, places=1)

    def test_mtbf_for_k_equal_1_is_14_comma_4(self):
        mtbf = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(1)
        self.assertAlmostEqual(mtbf, 14.4, places=1)

    def test_mtbf_for_k_equal_5_is_5_comma_8(self):
        mtbf = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(5)
        self.assertAlmostEqual(mtbf, 5.8, places=1)

    def test_mtbf_for_k_equal_20_is_9_comma_0(self):
        mtbf = DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_mtbf(20)
        self.assertAlmostEqual(mtbf, 9.0, places=1)


