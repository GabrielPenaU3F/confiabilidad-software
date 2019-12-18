import unittest

from src.domain.fitters.fitter import Fitter


class LogisticTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = Fitter().fit('logistic', 'ntds', initial_approx = (10, 0.05, 20))

    def test_ntds_logistic_least_squares_a_parameter_is_24_comma_611413(self):
        a = LogisticTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 24.611413, places=6)

    def test_ntds_logistic_least_squares_b_parameter_is_0_comma_041331(self):
        b = LogisticTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.041331, places=6)

    def test_ntds_logistic_least_squares_c_parameter_is_76_comma_485839(self):
        c = LogisticTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[2]
        self.assertAlmostEqual(c, 76.485839, places=6)

    def test_ntds_logistic_least_squares_prr_is_0_comma_181087(self):
        prr = LogisticTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 0.181087, places=6)
