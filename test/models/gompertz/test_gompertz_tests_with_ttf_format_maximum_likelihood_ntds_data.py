import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GompertzTestsWithTTFFormatMaximumLikelihoodNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('gompertz', 'ntds', initial_approx=(25, 0.5, 0.9), mts=False)

    def test_ntds_gompertz_maximum_likelihood_a_parameter_is_27_comma_973179(self):
        a = self.__class__.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.973179, places=6)

    def test_ntds_gompertz_maximum_likelihood_b_parameter_is_0_comma_036386(self):
        b = self.__class__.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.036386, places=6)

    def test_ntds_gompertz_maximum_likelihood_c_parameter_is_0_comma_981935(self):
        c = self.__class__.fit.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 0.981935, places=6)

    def test_ntds_gompertz_maximum_likelihood_prr_is_0_comma_580188(self):
        prr = self.__class__.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 0.580188, places=6)

    def test_ntds_gompertz_aic_is_168_comma_713381(self):
        aic = self.__class__.fit.get_aic()
        self.assertAlmostEqual(aic, 168.713381, places=6)
