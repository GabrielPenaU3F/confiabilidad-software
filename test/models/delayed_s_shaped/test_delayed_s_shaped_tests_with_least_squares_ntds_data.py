import unittest

from src.domain.fitters.fitter import TTFFitter


class DelayedSShapedTestsWithLeastSquaresNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('delayed-s-shaped', 'ntds', initial_approx=(1, 0.5))

    def test_ntds_delayed_s_shaped_least_squares_a_parameter_is_26_comma_715478(self):
        a = DelayedSShapedTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 26.715478, places=6)

    def test_ntds_delayed_s_shaped_least_squares_b_parameter_is_0_comma_021213(self):
        b = DelayedSShapedTestsWithLeastSquaresNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.021213, places=6)

    def test_ntds_delayed_s_shaped_least_squares_prr_is_2_comma_044758(self):
        prr = DelayedSShapedTestsWithLeastSquaresNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2.044758, places=6)
