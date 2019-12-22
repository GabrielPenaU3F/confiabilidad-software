import unittest

from src.domain.fitters.fitter import Fitter


class TestInitialCondition(unittest.TestCase):

    ttf_fit_ds = None
    fpd_fit_ds = None
    ttf_fit_go = None
    fpd_fit_go = None
    ttf_fit_log = None
    fpd_fit_log = None

    @classmethod
    def setUpClass(cls):
        #  x0 = 5 in ttf format means '0 failures reported at t=5'
        #  x0 = 5 in fpd format means '5 failures were present at t=0'
        cls.ttf_fit_ds = Fitter().fit('delayed-s-shaped', 'ntds', x0=5)
        cls.fpd_fit_ds = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', x0=5)
        cls.ttf_fit_go = Fitter().fit('goel-okumoto', 'ntds', x0=5)
        cls.fpd_fit_go = Fitter().fit('goel-okumoto', 'mixed-waterfall-agile', x0=5)
        cls.ttf_fit_log = Fitter().fit('logistic', 'ntds', x0=5)
        cls.fpd_fit_log = Fitter().fit('logistic', 'mixed-waterfall-agile', x0=5)

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

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_with_x0_equal_5_is_33_comma_611547(self):
        a = TestInitialCondition.ttf_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.611547, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_with_x0_equal_5_is_0_comma_006555(self):
        b = TestInitialCondition.ttf_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.006555, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_a_parameter_with_x0_equal_5_is_1414_comma_278491(self):
        a = TestInitialCondition.fpd_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1414.278491, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_b_parameter_with_x0_equal_5_is_0_comma_004757(self):
        b = TestInitialCondition.fpd_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.004757, places=6)

    def test_ntds_logistic_maximum_likelihood_a_parameter_with_x0_equal_5_is_24_comma_611413(self):
        a = TestInitialCondition.ttf_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.611413, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_with_x0_equal_5_is_0_comma_041331(self):
        b = TestInitialCondition.ttf_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.041331, places=6)

    def test_mixed_logistic_maximum_likelihood_a_parameter_with_x0_equal_5_is_835_comma_495462(self):
        a = TestInitialCondition.fpd_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 835.495462, places=6)

    def test_mixed_logistic_maximum_likelihood_b_parameter_with_x0_equal_5_is_0_comma_022889(self):
        b = TestInitialCondition.fpd_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.022889, places=6)
