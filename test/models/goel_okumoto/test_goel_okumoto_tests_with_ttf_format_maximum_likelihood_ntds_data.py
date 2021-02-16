import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GoelOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5), mts=False)

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_is_33_comma_993503(self):
        a = self.__class__.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.993503, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_is_0_comma_005790(self):
        b = self.__class__.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.005790, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_prr_is_1_comma_405048(self):
        prr = self.__class__.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1.405048, places=6)

    def test_ntds_goel_okumoto_aic_is_169_comma_380301(self):
        aic = self.__class__.fit.get_aic()
        self.assertAlmostEqual(aic, 169.380301, places=6)
