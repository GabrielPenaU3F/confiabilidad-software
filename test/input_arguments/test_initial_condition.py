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
        #  t0 = 5 in fpd format means '...'
        cls.ttf_fit_ds = Fitter().fit('delayed-s-shaped', 'ntds', t0=5)
        #cls.fpd_fit_ds = Fitter().fit('delayed-s-shaped', 'mixed-waterfall-agile', t0=5)
        cls.ttf_fit_go = Fitter().fit('goel-okumoto', 'ntds', t0=5)
        #cls.fpd_fit_go = Fitter().fit('goel-okumoto', 'mixed-waterfall-agile', t0=5)
        cls.ttf_fit_log = Fitter().fit('logistic', 'ntds', t0=5)
        #cls.fpd_fit_log = Fitter().fit('logistic', 'mixed-waterfall-agile', t0=2)

    def test_ntds_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_33_comma_590445(self):
        a = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 27.572573, places=6)

    def test_ntds_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_018699(self):
        b = TestInitialCondition.ttf_fit_ds.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.018699, delta=10**(-6))

    # def test_mixed_delayed_s_shaped_maximum_likelihood_a_parameter_with_t0_equal_5_is_935_comma_000664(self):
    #     a = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[0]
    #     self.assertAlmostEqual(a, 935.000664, places=6)
    #
    # def test_mixed_delayed_s_shaped_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_023049(self):
    #     b = TestInitialCondition.fpd_fit_ds.get_ml_parameters()[1]
    #     self.assertAlmostEqual(b, 0.023049, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_33_comma_529490(self):
        a = TestInitialCondition.ttf_fit_go.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 33.529490, places=6)

    def test_ntds_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_006599(self):
        b = TestInitialCondition.ttf_fit_go.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.006599, places=6)

    # def test_mixed_goel_okumoto_maximum_likelihood_a_parameter_with_t0_equal_5_is_1414_comma_278491(self):
    #     a = TestInitialCondition.fpd_fit_go.get_ml_parameters()[0]
    #     self.assertAlmostEqual(a, 1414.278491, places=6)
    #
    # def test_mixed_goel_okumoto_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_004757(self):
    #     b = TestInitialCondition.fpd_fit_go.get_ml_parameters()[1]
    #     self.assertAlmostEqual(b, 0.004757, places=6)

    def test_ntds_logistic_maximum_likelihood_a_parameter_with_t0_equal_5_is_24_comma_640875(self):
        a = TestInitialCondition.ttf_fit_log.get_ml_parameters()[0]
        self.assertAlmostEqual(a, 24.640875, places=6)

    def test_ntds_logistic_maximum_likelihood_b_parameter_with_t0_equal_5_is_0_comma_040930(self):
        b = TestInitialCondition.ttf_fit_log.get_ml_parameters()[1]
        self.assertAlmostEqual(b, 0.040930, places=6)

    def test_ntds_logistic_maximum_likelihood_c_parameter_with_t0_equal_5_is_76_comma_510170(self):
        c = TestInitialCondition.ttf_fit_log.get_ml_parameters()[2]
        self.assertAlmostEqual(c, 76.510170, places=6)

    # def test_mixed_logistic_maximum_likelihood_a_parameter_with_t0_equal_2_is_1242_comma_786355(self):
    #     a = TestInitialCondition.fpd_fit_log.get_ml_parameters()[0]
    #     self.assertAlmostEqual(a, 1242.786355, places=6)
    #
    # def test_mixed_logistic_maximum_likelihood_b_parameter_with_t0_equal_2_is_0_comma_016706(self):
    #     b = TestInitialCondition.fpd_fit_log.get_ml_parameters()[1]
    #     self.assertAlmostEqual(b, 0.016706, places=6)
    #
    # def test_mixed_logistic_maximum_likelihood_c_parameter_with_t0_equal_2_is_92_comma_333889(self):
    #     c = TestInitialCondition.fpd_fit_log.get_ml_parameters()[2]
    #     self.assertAlmostEqual(c, 92.333889, places=6)
