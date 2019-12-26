import unittest

from src.domain.fitters.model_fitter import ModelFitter


class MusaOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('musa-okumoto', 'ntds', initial_approx=(1, 0.5))

    def test_ntds_musa_okumoto_maximum_likelihood_a_parameter_is_23_comma_397375(self):
        a = MusaOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 23.397375, places=6)

    def test_ntds_musa_okumoto_maximum_likelihood_b_parameter_is_0_comma_008152(self):
        b = MusaOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.008152, places=6)

    def test_ntds_musa_okumoto_maximum_likelihood_prr_is_1_comma_558022(self):
        prr = MusaOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1.558022, places=6)

    def test_ntds_musa_okumoto_aic_is_169_comma_380301(self):
        aic = MusaOkumotoTestsWithTTFFormatMaximumLikelihoodNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 170.174757, places=6)
