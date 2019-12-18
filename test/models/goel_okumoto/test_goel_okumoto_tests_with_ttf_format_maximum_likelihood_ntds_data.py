import unittest

from src.domain.fitters.fitter import Fitter


class GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5))

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
