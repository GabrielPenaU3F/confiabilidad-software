import unittest

from src.domain.fitters.fitter import Fitter


class TestInitialCondition(unittest.TestCase):

    ttf_fit_ds = None
    fpd_fit_ds = None

    @classmethod
    def setUpClass(cls):
        #  x0 = 5 in ttf format means '0 failures reported at t=5'
        cls.ttf_fit_ds = Fitter().fit('delayed-s-shaped', 'ntds', x0=5)
        #  x0 = 5 in fpd format means '5 failures were present at t=0'
        cls.fpd_fit_ds = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', x0=5)

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_with_x0_equal_5_is_33_comma_590445(self):
        a = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.572573, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_with_x0_equal_5_is_0_comma_018699(self):
        b = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.018699, delta=10**(-6))

    def test_mixed_delayed_s_shaped_maximum_likelihood_a_parameter_with_x0_equal_5_is_935_comma_000664(self):
        a = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 935.000664, places=6)

    def test_mixed_delayed_s_shaped_maximum_likelihood_b_parameter_with_x0_equal_5_is_0_comma_023049(self):
        b = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.023049, places=6)
