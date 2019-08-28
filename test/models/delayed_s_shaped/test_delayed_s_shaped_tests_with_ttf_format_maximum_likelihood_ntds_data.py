import unittest

from src.fitters.fitter import TTFFitter


class DelayedSShapedTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('delayed-s-shaped', 'ntds')

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