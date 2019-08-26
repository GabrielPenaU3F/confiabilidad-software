import unittest

from src.fitters.fitter import TTFFitter


class DelayedSShapedTestsWithNtdsData(unittest.TestCase):

    fit = None

    @classmethod
    def setUpClass(cls):
        cls.fit = TTFFitter().fit('delayed-s-shaped', 'ntds')

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_is_27_comma_491544(self):
        a = DelayedSShapedTestsWithNtdsData.fit.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.491544, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_is_0_comma_018579(self):
        b = DelayedSShapedTestsWithNtdsData.fit.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.018579, places=6)

    def test_ntds_delayed_s_shaped_least_squares_a_parameter_is_26_comma_715478(self):
        a = DelayedSShapedTestsWithNtdsData.fit.get_lsq_parameters()[0]
        self.assertAlmostEqual(a, 26.715478, places=6)

    def test_ntds_delayed_s_shaped_least_squares_b_parameter_is_0_comma_021213(self):
        b = DelayedSShapedTestsWithNtdsData.fit.get_lsq_parameters()[1]
        self.assertAlmostEqual(b, 0.021213, places=6)

    def test_ntds_delayed_s_shaped_least_squares_prr_is_2_comma_044758(self):
        prr = DelayedSShapedTestsWithNtdsData.fit.get_prr_lsq()
        self.assertAlmostEqual(prr, 2.044758, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_prr_is_3_comma_990516(self):
        prr = DelayedSShapedTestsWithNtdsData.fit.get_prr_ml()
        self.assertAlmostEqual(prr, 3.990516, places=6)

    def test_ntds_delayed_s_shaped_aic_is_163_comma_835957(self):
        aic = DelayedSShapedTestsWithNtdsData.fit.get_aic()
        self.assertAlmostEqual(aic, 163.835957, places=6)
