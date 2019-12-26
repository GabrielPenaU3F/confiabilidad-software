import unittest

from src.domain.fitters.model_fitter import ModelFitter


class LogisticTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = ModelFitter().fit('logistic', 'ntds', initial_approx=(10, 0.05, 20), lsq_only=True)

    def test_ntds_logistic_least_squares_a_parameter_is_24_comma_640875(self):
        a = LogisticTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 24.640875, places=6)

    def test_ntds_logistic_least_squares_b_parameter_is_0_comma_040930(self):
        b = LogisticTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.040930, places=6)

    def test_ntds_logistic_least_squares_c_parameter_is_76_comma_510170(self):
        c = LogisticTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 76.510170, places=6)

    def test_ntds_logistic_least_squares_prr_is_0_comma_181087(self):
        prr = LogisticTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 0.193478, places=6)
