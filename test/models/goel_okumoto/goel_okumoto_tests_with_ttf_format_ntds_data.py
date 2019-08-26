import unittest

from src.fitters.fitter import TTFFitter


class GoelOkumotoTestsWithTTFFormatNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('goel-okumoto', 'ntds')

    def test_ntds_goel_okumoto_least_squares_a_parameter_is_33_comma_599359(self):
        a = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 33.599359, places=6)

    def test_ntds_goel_okumoto_least_squares_b_parameter_is_0_comma_006296(self):
        b = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.006296, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_is_33_comma_993503(self):
        a = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.993503, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_is_0_comma_005790(self):
        b = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.005790, places=6)

    def test_ntds_goel_okumoto_least_squares_prr_is_1_comma_507181(self):
        prr = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.507181, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_prr_is_1_comma_405048(self):
        prr = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 1.405048, places=6)

    def test_ntds_goel_okumoto_aic_is_167_comma_380301(self):
        aic = GoelOkumotoTestsWithTTFFormatNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 167.380301, places=6)
