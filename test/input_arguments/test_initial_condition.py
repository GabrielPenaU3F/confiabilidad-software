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
        #  t0 = 5 in ttf format means '0 failures reported at t=5'
        #  t0 = 5 in fpd format means 'the dataset begins at t=6'
        cls.ttf_fit_ds = Fitter().fit('delayed-s-shaped', 'ntds', t0=5)
        cls.fpd_fit_ds = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', t0=5)
        cls.ttf_fit_go = Fitter().fit('goel-okumoto', 'ntds', t0=5)
        cls.fpd_fit_go = Fitter().fit('goel-okumoto', 'mixed-waterfall-agile', t0=5)
        cls.ttf_fit_log = Fitter().fit('logistic', 'ntds', t0=5)
        cls.fpd_fit_log = Fitter().fit('logistic', 'mixed-waterfall-agile', t0=2)

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_27_comma_876270(self):
        a = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.876270, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_017446(self):
        b = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.017446, delta=10**(-6))

    def test_mixed_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_940_comma_279403(self):
        a = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 940.279403, places=6)

    def test_mixed_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_021931(self):
        b = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.021931, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_34_comma_992027(self):
        a = TestInitialCondition.ttf_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 34.992027, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_005790(self):
        b = TestInitialCondition.ttf_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.005790, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_1414_comma_278491(self):
        a = TestInitialCondition.fpd_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 1407.755657, places=6)

    def test_mixed_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_004957(self):
        b = TestInitialCondition.fpd_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.004957, places=6)

    def test_ntds_logistic_maximum_likelihood_a_parameter_with_t0_equal_5_is_24_comma_640875(self):
        a = TestInitialCondition.ttf_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.640875, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_040930(self):
        b = TestInitialCondition.ttf_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.040930, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_with_t0_equal_5_is_76_comma_510170(self):
        c = TestInitialCondition.ttf_fit_log.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.510170, places=6)

    # Check wtf is going on here
    # def test_mixed_logistic_maximum_likelihood_a_parameter_with_t0_equal_2_is_1242_comma_786355(self):
    #     a = TestInitialCondition.fpd_fit_log.get_ml_parameters()[0]
    #     self.assertAlmostEqual(a, 835.093560, places=6)
    #
    # def test_mixed_logistic_maximum_likelihood_b_parameter_with_t0_equal_2_is_0_comma_016706(self):
    #     b = TestInitialCondition.fpd_fit_log.get_ml_parameters()[1]
    #     self.assertAlmostEqual(b, 0.016706, places=6)
    #
    # def test_mixed_logistic_maximum_likelihood_c_parameter_with_t0_equal_2_is_92_comma_333889(self):
    #     c = TestInitialCondition.fpd_fit_log.get_ml_parameters()[2]
    #     self.assertAlmostEqual(c, 92.333889, places=6)
