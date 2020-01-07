import unittest

from src.domain.fitters.model_fitter import ModelFitter


class MusaOkumotoTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('musa-okumoto', 'ntds', initial_approx=(1, 0.5), lsq_only=True)

    def test_ntds_musa_okumoto_least_squares_a_parameter_is_20_comma_926172(self):
        a = MusaOkumotoTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 20.926172, places=6)

    def test_ntds_musa_okumoto_least_squares_b_parameter_is_0_comma_010806(self):
        b = MusaOkumotoTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.010806, places=6)

    def test_ntds_musa_okumoto_least_squares_prr_is_1_comma_619832(self):
        prr = MusaOkumotoTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 1.619832, places=6)
