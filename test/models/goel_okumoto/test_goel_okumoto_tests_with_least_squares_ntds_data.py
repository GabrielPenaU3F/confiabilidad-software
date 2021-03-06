import unittest

from src.domain.fitters.model_fitter import ModelFitter


class GoelOkumotoTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('goel-okumoto', 'ntds', initial_approx=(1, 0.5), lsq_only=True, mts=False)

    def test_ntds_goel_okumoto_least_squares_a_parameter_is_33_comma_599461(self):
        a = self.__class__.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 33.599461, places=6)

    def test_ntds_goel_okumoto_least_squares_b_parameter_is_0_comma_006296(self):
        b = self.__class__.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.006296, places=6)

    def test_ntds_goel_okumoto_least_squares_prr_is_1_comma_507177(self):
        prr = self.__class__.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.507177, places=6)
